import torch
from torch import nn
from torchtext.legacy import data
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
from torch.utils.data import DataLoader
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import soundfile as sf
import os

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# ASR Model
asr_model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h").to(device)
asr_tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-large-960h")

# Loading the dataset
df = pd.read_csv('../Dataset/classification_details.txt', delimiter='||', header=None, names=['audio_file_name', 'classification', 'subclassification', 'conversational_history'])

# Label encoding the classification column
le = LabelEncoder()
df['classification'] = le.fit_transform(df['classification'])

# Create Fields
LABEL = data.LabelField(dtype = torch.float)

# Speech to Text
def speech_to_text(file):
    file = os.path.join('../Audio', file)
    speech, _ = sf.read(file)
    input_values = asr_tokenizer(speech, return_tensors="pt").input_values
    logits = asr_model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcriptions = asr_tokenizer.decode(predicted_ids[0])
    return transcriptions

df['text'] = df['audio_file_name'].apply(lambda x: speech_to_text(x))

fields = [('text', data.Field(tokenize='spacy', include_lengths=True)), ('classification', LABEL)]

examples = [data.Example.fromlist([df.text[i],df.classification[i]], fields) for i in range(df.shape[0])] 
dataset = data.Dataset(examples, fields)

# Splitting the dataset
train_data, valid_data = dataset.split(split_ratio=0.8)

# Building vocab and loading the iterator
data.Field.build_vocab(train_data, max_size = 25000, vectors = "glove.6B.100d")
LABEL.build_vocab(train_data)

BATCH_SIZE = 64
train_iterator, valid_iterator = data.BucketIterator.splits(
    (train_data, valid_data), 
    batch_size = BATCH_SIZE,
    sort_within_batch = True,
    device = device)

# LSTM Classifier
class Classifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim, n_layers, 
                 bidirectional, dropout):
        
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.LSTM(embedding_dim, 
                           hidden_dim, 
                           num_layers=n_layers, 
                           bidirectional=bidirectional, 
                           dropout=dropout)
        self.fc = nn.Linear(hidden_dim * 2, output_dim)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, text, text_lengths):
        embedded = self.dropout(self.embedding(text))
        packed_embedded = nn.utils.rnn.pack_padded_sequence(embedded, text_lengths)
        packed_output, (hidden, cell) = self.rnn(packed_embedded)
        hidden = self.dropout(torch.cat((hidden[-2,:,:], hidden[-1,:,:]), dim = 1))
        return self.fc(hidden.squeeze(0))

# Creating an instance of our model
classifier_model = Classifier(len(data.Field.vocab), 100, 256, 1, 2, True, 0.5).to(device)

# Training the model
optimizer = torch.optim.Adam(classifier_model.parameters())
criterion = nn.BCEWithLogitsLoss()

def binary_accuracy(preds, y):
    rounded_preds = torch.round(torch.sigmoid(preds))
    correct = (rounded_preds == y).float()
    acc = correct.sum() / len(correct)
    return acc

def train(model, iterator, optimizer, criterion):
    epoch_loss = 0
    epoch_acc = 0
    model.train()
    
    for batch in iterator:
        optimizer.zero_grad()
        text, text_lengths = batch.text
        predictions = model(text, text_lengths).squeeze(1)
        loss = criterion(predictions, batch.label)
        acc = binary_accuracy(predictions, batch.label)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
        epoch_acc += acc.item()
        
    return epoch_loss / len(iterator), epoch_acc / len(iterator)

# train 
N_EPOCHS = 5

for epoch in range(N_EPOCHS):
    train_loss, train_acc = train(classifier_model, train_iterator, optimizer, criterion)
    print(f'Epoch: {epoch+1}, Train Loss: {train_loss:.3f}, Train Acc: {train_acc*100:.2f}%')


# MOVE THIS INFERENCE CODE OUTSIDE OF THIS FILE
# inference
def classify_audio(file_path):
    asr_model.eval()
    classifier_model.eval()
    
    with torch.no_grad():
        # 1. Speech to Text
        speech, _ = sf.read(file_path)
        input_values = asr_tokenizer(speech, return_tensors="pt").input_values
        logits = asr_model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = asr_tokenizer.decode(predicted_ids[0])

        # 2. Text to Classification
        tokenized = [tok.text for tok in data.Field.tokenizer(transcription)]
        indexed = [data.Field.vocab.stoi[t] for t in tokenized]
        length = [len(indexed)]
        tensor = torch.LongTensor(indexed).to(device)
        tensor = tensor.unsqueeze(1).T
        length_tensor = torch.LongTensor(length)
        prediction = torch.sigmoid(classifier_model(tensor, length_tensor))
        
        return le.inverse_transform([round(prediction.item())])
