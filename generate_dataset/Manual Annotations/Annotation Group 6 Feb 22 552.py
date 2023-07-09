"""
- 06:46.7 very tough between content and action

- 07:01.2 & 07:14.7 Action is difficult when conditional ('would') is introduced. It blurs the line but we choose action

- 08:02.8 difficult between backchannel and interruption but it is a statement so this is backchannel
- 08:19.8 good example of interruption concerning action

[???]
- 09:09.4 : agreement is not an action. But usually in answering questions we would want the chatbot to be sent to Dialogue Manager (hence action)
"""
data = [
    {
        'startTime' : '00:43.6',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '00:55.5',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '01:01.6',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '01:12.1',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '01:19.3',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '01:29.1',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '01:36.6',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '02:02.0',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '02:07.3',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '02:08.9',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '02:16.2',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '02:18.2',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '02:25.6',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '02:47.6',
        'speakerId' : 'Green',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '02:58.4',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '03:01.1',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '03:37.7',
        'speakerId' : 'Orange',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '03:39.1',
        'speakerId' : 'Green',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '03:43.8',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'noise'
    },
    {
        'startTime' : '04:00.0',
        'speakerId' : 'Green',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '04:01.8',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '04:15.4',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '04:23.1',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '04:39.7',
        'speakerId' : 'Green',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '04:57.0',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '04:59.0',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '05:34.8',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '05:40.8',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '05:54.6',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '06:21.0',
        'speakerId' : 'Pink',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '06:46.7',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '06:50.6',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '07:01.2',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '07:10.0',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '07:30.0',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '07:44.2',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '07:48.3',
        'speakerId' : 'Pink',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    },
    {
        'startTime' : '08:02.8',
        'speakerId' : 'Blue',
        'classification' : 'non-interruption',
        'sub-classification' : 'backchannel'
    },
    {
        'startTime' : '08:13.2',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '08:19.8',
        'speakerId' : 'Blue',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '08:59.9',
        'speakerId' : 'Orange',
        'classification' : 'interruption',
        'sub-classification' : 'concerning action'
    },
    {
        'startTime' : '09:09.4',
        'speakerId' : 'Green',
        'classification' : 'interruption',
        'sub-classification' : 'concerning content'
    }
]