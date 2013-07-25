import twitter
import util

PHILLY_WOEID = 2471217
#READ ONLY CREDS TO THE PYSTAR TWITTER STREAM
CONSUMER_KEY = '4Aq8dWoPUgErnEbkGTEVA'
CONSUMER_SECRET = 'We will give this to you in class :)'
ACCESS_TOKEN_KEY = '312791763-4Gi0iN2R4AbPofQMxIXAX64SzUrKZuVSEQchXglRp'
ACCESS_TOKEN_SECRET = '5Iq6x4Pqo0kM9fYdCssKGwTgQMtmjF3ugFKydu0fspE'

def search(searchTerm):
    """
    Print recent tweets containing `searchTerm`.

    To test this function, at the command line run:
        python twitter_api.py --search=<search term>
    For example,
        python twitter_api.py --search=python
    """
    api = twitter.Api(consumer_key = CONSUMER_KEY,
                      consumer_secret = CONSUMER_SECRET,
                      access_token_key = ACCESS_TOKEN_KEY,
                      access_token_secret = ACCESS_TOKEN_SECRET)

    tweets = api.GetSearch(searchTerm)
    for tweet in tweets:
        util.safe_print(tweet.GetText())

def trendingTopics():
    """
    Print the currently trending topics.

    To test this function, at the command line run:
        python twitter_api.py -t
    """
    api = twitter.Api(consumer_key = CONSUMER_KEY,
                  consumer_secret = CONSUMER_SECRET,
                  access_token_key = ACCESS_TOKEN_KEY,
                  access_token_secret = ACCESS_TOKEN_SECRET)

    trending_topics = api.GetTrendsWoeid(PHILLY_WOEID)
    for topic in trending_topics:
        util.safe_print(topic.name)

def userTweets(username):
    """
    Print recent tweets by `username`.

    You may find the twitter.Api() function GetUserTimeline() helpful.

    To test this function, at the command line run:
        python twitter_api.py -u <username>
    For example,
        python twitter_api.py -u PyStarPhilly
    """
    pass

def trendingTweets():
    """
    Print tweets for all the trending topics.

    To test this function, at the command line run:
        python twitter_api.py -w
    """
    pass
