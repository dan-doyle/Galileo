# Currently we don't include the full file after the last segment of audio e.g. if the length is 600 and segment_length = 500 we only have one file from 0 to 500
import os
import csv
from collections import deque
from pydub import AudioSegment

# example filepath: './Transcripts/Transcript Group 1 Feb 8 429.txt'
def retrieve_details(filepath, speaker, start_time, num_prev):
    """
    Function that retrieves the previous utterances and end time for a given utterance
    This is a helper function that deals specifically with GAP dataset
    """
    with open(filepath, 'r') as f:
        reader = csv.reader(f, delimiter='\t')  # assuming the file is tab-separated
        next(reader)  # skip the header
        users = {}
        conversation_history = deque(maxlen=num_prev)
        for row in reader:
            curr_speaker = row[0].split('.')[1]
            if curr_speaker == speaker and row[1] == start_time:
                return row[2], conversation_history
            conversation_history.append(row[3])

def time_to_ms(time_str):
    """Convert a string in format mm:ss.s to milliseconds."""
    # Split the input string into minutes and seconds
    minutes, seconds = time_str.split(":")

    # Convert minutes and seconds to milliseconds and return the sum
    return int(minutes) * 60000 + float(seconds) * 1000

audio_filepath = './Audio/MP4 Group 1 Feb 8 429.mp4.wav'
# replace X with a more appropriate name
# here we only have
def extract_audio(audio_filepath, start_time, end_time, X, conversational_history, classification, subclassification):
    # To-do: reduce hard coding with filepaths
    dataset_dir = os.path.join(os.getcwd(), '../dataset')
    # Check if the '/Dataset' directory exists
    if not os.path.exists(dataset_dir):
        # Create the '/Dataset' directory
        os.mkdir(dataset_dir)
        os.mkdir(os.path.join(dataset_dir, 'audio'))

    # Determine the group number from the audio file path
    group_number = os.path.basename(audio_filepath).split(' ')[2]  # Assumes the group number is always the third element of the file name

    # Load the audio file
    audio = AudioSegment.from_wav(audio_filepath)

    # Convert start and end times to milliseconds
    start_time_ms = time_to_ms(start_time)
    end_time_ms = time_to_ms(end_time)
    
    # Determine the number of audio files to save
    duration = end_time_ms - start_time_ms
    num_files = int(duration // X)

    segment_end_time_ms = start_time_ms # initialise for the loop
    # split the file per X milliseconds
    for i in range(1, num_files+1):
        # Determine the start and end times for this segment
        segment_end_time_ms = min(segment_end_time_ms + X, end_time_ms) # this min shouldnt be needed
        
        # Extract segment
        segment = audio[start_time_ms:segment_end_time_ms]

        # Format the file name
        file_name = f"Group {group_number}: {start_time} - {end_time} - {i}.wav"
        
        # Set the output file path
        output_filepath = os.path.join("../dataset/audio", file_name)

        # Ensure the directory exists
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

        # Export segment
        segment.export(output_filepath, format="wav")
        
        # Append to the text file
        with open(os.path.join('../dataset', 'classification_details.txt'), 'a') as f:
            f.write(f"{file_name}||{classification}||{subclassification}||{conversational_history}\n")

def create_dataset(segment_length, num_prev):
    # loop through all files in Manual Annotations REPLACE
    for filename in os.listdir(os.path.join(os.getcwd(), 'Manual Annotations')):
        # now loop through the list of annotation objects and call extract audio for each one!
        file_path = os.path.join(os.getcwd(), 'Manual Annotations', filename)
        # print(file_path)
        if filename.startswith('Annotation'):
            print('Viewing: ', filename)
            with open(file_path, 'r') as file:
                    script = file.read()
            exec(script, globals()) # introduces 'data' variable

            # extract filename
            audio_filepath = './Audio/' + filename.replace('Annotation', 'MP4').replace('.py', '.mp4.wav')
            # Loop through each object in the data list and print the speakerId
            for annotation in data:
                start_time = annotation['startTime']
                classification = annotation['classification']
                subclassification = annotation['sub-classification']
                transcript_filepath = './Transcripts/' + filename.replace('Annotation', 'Transcript').replace('.py', '.txt')
                end_time, conversational_history = retrieve_details(transcript_filepath, annotation['speakerId'], start_time, num_prev)
                # FIX NEEDED for conversational history being a list
                extract_audio(audio_filepath, start_time, end_time, segment_length, conversational_history[0], classification, subclassification)
            break # Remove when finished testing

        
# from the generate dataset directory, run python3 extract_dataset_audio
if __name__ == "__main__":
    create_dataset(300, 1)