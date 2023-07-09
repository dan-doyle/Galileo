"""
Can we split up: 'Can you rephrase that?' and 'Can you turn off the DO?' It may be difficult to teach the model to differentiate given the lack of examples
    - One is elicit clarification and the other an instruction not too disimilar from request permission

02:55.4 - shows the interruption does not have to be successful, just that there is intent to take the turn

03:17.8 - similar to a rush but not, would the model pick this up
"""
data = [
    {
        'startTime' : '00:11.6',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '00:12.9',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '00:20.8',
        'speakerId' : 'Yellow',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '00:33.6',
        'speakerId' : 'Yellow',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '00:35.0',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '00:50.9',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '00:51.5',
        'speakerId' : 'Yellow',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '01:09.8',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '01:42.4',
        'speakerId' : 'Yellow',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '02:03.6',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '02:06.6',
        'speakerId' : 'Yellow',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '02:21.5',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '02:29.6',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '02:35.9',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '02:43.6',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '02:55.4',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '03:04.3',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '03:17.8',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '03:49.2',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    }
]