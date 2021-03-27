import tweepy
from tweepy import OAuthHandler
import re 

class TwitterClient(object):
    '''
    Twitter Class for grabbing Tweets
    '''
    def __init__(self):
        '''
        Initialization Method
        '''
        #Keys and Tokens from the Twitter Dev Console
        consumer_key = 'osoPe1vbrjL6hi83pPaT99JcZ'
        consumer_secret = '72ePjiWIu8YGRFSTXJdUiww12J6UcR0bJL556VSx73hfd7dwW0'
        access_token = '1038587928967098368-uX8QbeIua1pXU33gzB5Tcy89qMPrgt'
        access_token_secret = 'AohvvdBfkYILiwEouMpAfyVDP2TBX6xdLcmfyvAJqojcj'

        #Attempt Authentication
        try:
            #Create OAuthhandler object
            self.auth = OAuthHandler(consumer_key,consumer_secret)
            #Set access token and secret 
            self.auth.set_access_token(access_token,access_token_secret)
            #Create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error Authentication Failed")
    
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    
    def get_tweets(self, query, count = 1):
        '''
        Main Function to fetch tweets and parse them
        '''
        #Empty list to store parsed tweets
        tweets = []

        try:
            #call twitter api to fetch tweets
            fetch_tweets = self.api.search(q=query,count = count)
            
            #parsing tweets one by one
            for tweet in fetch_tweets:
                print(tweet)
                #empty dictionary to store required params of tweet
                parsed_tweet = {}

                #saving text of tweet
                parsed_tweet['text'] = tweet.text
               
                #appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    #if tweet has a retweet, ensure that is is append only once.
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                    else:
                        tweets.append(parsed_tweet)
                
                #return parsed tweet
                return tweets
        except tweepy.TweepError as e:
            #print error
            print("Error : " + str(e))

def main():
    #Creating Object of twitter client class
    api = TwitterClient()
    #calling function to get tweets
    tweets = api.get_tweets(query = 'Cryptocurrency', count = 1)

    #print tweets
    print(tweets)

#running program
main()