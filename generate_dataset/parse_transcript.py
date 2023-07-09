from collections import deque
import time
import sys
from datetime import datetime, timedelta
import csv
import json
import os
from dotenv import load_dotenv
import numpy as np

# Load environment variables from .env
load_dotenv()

# implement strategy / adapter pattern with functions to deal with parsing different datasets

def parse_GAP_file(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter='\t')  # assuming the file is tab-separated
        next(reader)  # skip the header
        users = {}
        for row in reader:
            data.append(row)
            speaker_colour = row[0].split('.')[1]
            if speaker_colour not in users:
                users[speaker_colour] = len(users) + 1
            data[-1][0] = users[speaker_colour]
    return data


# Extract out functionality into an Utterance class, so this can be returned by the function instead of the current object
class UtteranceIterator: # make an actual iterator
    """
    Logic:
        - Only when a new speaker speaks, we output the last 4 conversational turns
        Edge cases:
            - Process all available utterances when context-length isn't available at the beginning
            - First utterance cannot be an interruption hence is not returned
    To do:
        - Deal with special characters such as '$': create a helper for this
    """
    def __init__(self, data, context_length = 5):
        self.context_length = context_length
        self.data = data
        self.conversation_history = deque(maxlen=self.context_length) # expand this to contain timestamps etc and audio name
        self.current_speaker = None
        self.current_timestamp = None
        self.prev_timestamp = None
        self.current_overlap = False
        self.short_pause = False
        self.index = 0

    # Change so this processes utterance rather than sentence (whatever that means?)
    def _process_utterance(self, utterance, include_speaker):
        participant = utterance[0]
        utterance[3] = utterance[3].replace('$', '[laughter]')
        overlap = ''
        short_pause = '[short pause] ' if self.short_pause else ''
        return "\nSpeaker " + f'{participant}: {overlap}{short_pause}{utterance[3]}' if include_speaker else f' {utterance[3]}'

    def get_conversation(self):
        if self.index < len(self.data): # find more elegant way than iterator
            unprocessed_utterance = self.data[self.index]
            self.current_speaker = unprocessed_utterance[0]
            self.current_timestamp = unprocessed_utterance[1:3]
            if self.index > 0:
                self.current_overlap = self.check_overlap()
                self.short_pause = self.check_pause(unprocessed_utterance[1])
            utterance = self._process_utterance(unprocessed_utterance, True)
            self.conversation_history.append(utterance)
            self.index += 1

            result = {}
            # remove speech that is not attributed to a speaker
            while 'Speaker' not in self.conversation_history[0]:
                self.conversation_history.popleft()
            result['transcript'] = ''.join(list(self.conversation_history))
            result['timestamp'] = self.current_timestamp
            result['overlap'] = self.current_overlap
            self.current_overlap = False
            self.short_pause = False
            self.prev_timestamp = self.current_timestamp
            return result
        else:
            return None     

    def check_overlap(self):
        # Extract this processing code to a helper as it is used multiple times
        prev_end_time = self.prev_timestamp[1]
        prev_start_time = self.prev_timestamp[0]
        curr_end_time = self.current_timestamp[1]
        curr_start_time = self.current_timestamp[0]

        # Convert time strings to datetime objects
        prev_start_datetime = datetime.strptime(prev_start_time, "%M:%S.%f")
        prev_end_datetime = datetime.strptime(prev_end_time, "%M:%S.%f")
        curr_start_datetime = datetime.strptime(curr_start_time, "%M:%S.%f")
        curr_end_datetime = datetime.strptime(curr_end_time, "%M:%S.%f")

        # we only count overlaps that are not in the first 300ms or last 10% of speech
        basic_overlap_condition = prev_start_datetime < curr_end_datetime
        if curr_start_time == "00:09.8":
            print('prev_start_time: ', prev_start_time)
            print('prev_end_time: ', prev_end_time)
            print('curr_start_time: ', curr_start_time)
            print('curr_end_time: ', curr_end_time)
            print('difference: ', (curr_start_datetime - prev_start_datetime))
        immediate_overlap_condition = (curr_start_datetime - prev_start_datetime).total_seconds() > 0.3

        prev_utterance_duration = prev_end_datetime - prev_start_datetime
        early_onset_deadline = prev_end_datetime - (prev_utterance_duration / 10)
        not_early_onset_condition = curr_start_datetime < early_onset_deadline

        if basic_overlap_condition and immediate_overlap_condition and not_early_onset_condition:
        # if basic_overlap_condition:
            return True
        return False

    
    def check_pause(self, new_time):
        curr_time = self.current_timestamp[1]

        # Convert time strings to datetime objects
        curr_datetime = datetime.strptime(curr_time, "%M:%S.%f")
        new_datetime = datetime.strptime(new_time, "%M:%S.%f")

        # Calculate the time difference
        time_difference = new_datetime - curr_datetime

        # Check if the time difference is greater than 2 seconds
        if time_difference > timedelta(seconds=2):
            return True
        
        return False

def parse_response(response):
    start_index = response.find('<class>') + len('<class>')
    end_index = response.rfind('</class>')
    if start_index == -1 or end_index == -1:
        raise ValueError("Invalid response format: No JSON object found")
    
    result = response[start_index:end_index]
    return result

# reduce duplication by combining into parse_response
def extract_reflection(response):
    start_index = response.find('<reflection>') + len('<reflection>')
    end_index = response.rfind('</reflection>')
    if start_index == -1 or end_index == -1:
        raise ValueError("Invalid response format: No JSON object found")
    
    result = response[start_index:end_index]
    return result

data = parse_GAP_file('./Transcripts/Transcript Group 11 June 6 1219.txt')

if __name__ == "__main__":
    output = ""
    completed = True
    c = UtteranceIterator(data)
    curr = c.get_conversation()
    i = 1
    overlap_count = 0
    while curr is not None:
        if curr['overlap']:
            output += curr['timestamp'][0]
            output += curr['transcript'] + '\n\n'
            overlap_count += 1
        i += 1
        curr = c.get_conversation()

    print('OVERLAP COUNT:', overlap_count, 'Out of:', i)

    with open('current_overlaps.txt', 'w') as file:
        file.write(output)