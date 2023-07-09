"""
regarding 01:28.1: if it is concerning content how do we tell the difference between:
    - Uh, do you want a pencil just in case we change anything? Sure
    - Do you want me to turn off the DO? Sure
Our approach can't be to label any answer as 'concerning action'

05:45.5 & 05:56.4 - concerning action because it is an instruction of sorts

09:50.7 & 10:27.2 - noise with a cough, the vast majority of 'noise' is laughter so we need to find more of a balance
"""
data = [
    {
        'startTime' : '01:03.1',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '01:28.1',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '01:41.5',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '01:45.4',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '02:28.3',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '03:03.3',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '03:40.9',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '03:52.4',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '03:56.4',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '04:24.7',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '05:02.3',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '05:17.1',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '05:45.5',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '05:56.4',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '06:04.1',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '06:09.3',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '06:09.9',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '06:35.0',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '06:36.7',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '06:39.3',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '06:40.1',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'noise'
    },
    {
        'startTime' : '06:45.7',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '06:54.4',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '07:01.3',
        'speakerId' : 'Yellow',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '07:03.8',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '08:34.8',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '08:51.2',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '08:57.7',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '09:14.4',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '09:38.4',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '09:50.7',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'noise'
    },
    {
        'startTime' : '10:00.9',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '10:27.2',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'noise'
    },
    {
        'startTime' : '11:35.2',
        'speakerId' : 'Yellow',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '11:42.2',
        'speakerId' : 'Yellow',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    }
]