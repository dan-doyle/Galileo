"""
In write-up, the first two are good examples of the subtleties of backchannel and how context is important
A good way to distinguish backchannel vs and interruption giving an answer, is if 1) there was a *question* and 2) if was no overlap, would it constitute and answer? If so it is not backchannel

A few cases where there is agreement but it is hard to classify between action and content: 01:07.4 & 01:24.5 & 01:45.1 & 02:01.8
    - Not content if there is an action suggested directly before by interruptee through a verb e.g. 'putting', 'having' and the interupter determines whether it happens or not. 01:24.5 is the most difficult to assign
"""
data = [
    {
        'startTime' : '00:03.7',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '00:15.7',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '01:07.4',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '01:17.0',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '01:24.5',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '01:45.1',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '01:54.1',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '01:58.4',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '02:01.8',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '02:17.2',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '02:18.6',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    }
]