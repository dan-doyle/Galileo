"""
- 02:09.2: content (add detail) NOT related to an action being taken BY THE PERSON SPEAKING AT THAT MOMENT, need to clear this up across the board
- 02:42.1: Good example of doesn't have to be successful
- 03:13.4: not action
- 03:29.6 good example of interruption concerning action as THE PERSON SPEAKING AT THAT MOMENT is taking an action
- tricky: 03:59.4 & 07:35.1 & 08:29.0 action vs content
- 05:45.2: perfect example of action not content (agreement)
- 05:55.1: have it as action
"""
data = [
    {
        'startTime' : '00:10.6',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '00:15.3',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '00:27.4',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '00:33.7',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '00:36.0',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '01:10.5',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '01:13.0',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '01:19.5',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '01:22.1',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '01:27.8',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '01:52.5',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '02:00.2',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '02:09.2',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '02:34.4',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'noise'
    },
    {
        'startTime' : '02:42.1',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '02:52.6',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '03:08.4',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '03:13.4',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '03:17.5',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '03:29.6',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '03:59.4',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '04:21.4',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '04:26.1',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '04:42.1',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '04:50.9',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '05:24.3',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '05:37.0',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '05:45.2',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '05:55.1 ',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '05:58.8',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '06:08.2',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '06:51.4',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '06:59.6',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '07:02.5',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '07:19.1',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '07:33.7',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '07:35.1',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '07:39.0',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '08:12.0',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '08:16.4',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '08:29.0',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '08:51.4',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    }
]