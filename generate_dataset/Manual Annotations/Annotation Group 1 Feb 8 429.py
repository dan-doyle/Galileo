"""
- 02:43.5
- 06:02.5 + 07:13.6: interruption concerning a communicative action (rush), it could be hard for the model to learn what the distinction is
- 5:56.1: misplaced speech, should have been filtered out
"""
data = [
    {
        'startTime' : '00:23.9',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '00:24.3',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '00:35.4',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '00:37.0',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '01:08.6',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '01:09.8',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '01:25.3',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '01:31.5',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '01:46.4',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '01:49.0',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'noise'
    },
    {
        'startTime' : '01:51.0',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '01:55.3',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '02:11.1',
        'speakerId' : 'Green',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '02:22.1',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'noise'
    },
    {
        'startTime' : '02:30.1',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '02:30.7',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'noise'
    },
    {
        'startTime' : '02:32.6',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '02:43.5',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '02:45.7',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'noise'
    },
    {
        'startTime' : '03:14.4',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '03:20.3',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'noise'
    },
    {
        'startTime' : '03:31.4',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '03:33.0',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'noise'
    },
    {
        'startTime' : '03:45.0',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '04:24.1',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '04:26.9',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '04:54.4',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '05:01.4',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '05:08.2',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'noise'
    },
    {
        'startTime' : '05:08.9',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '05:13.8',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '05:22.6',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '05:23.6',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '06:00.2',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '06:02.5',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '06:44.6',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '07:01.2',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '07:08.6',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '07:10.5',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '07:13.6',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '07:35.6',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '07:58.9',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '08:25.9',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '08:37.9',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '09:24.6',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    }
]