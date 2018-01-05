__author__ = 'prakhardogra'

import tweepy
#from twython import Twython, TwythonError
import json
import time
from cleaner import clean
from checker import check
from math import sqrt
from classify import get_classifier_MNB
from fs import get_feature_set
import gttd

consumer_key = "RGVO3CTujE60TW5IQy1JwmyxF"
consumer_secret = "ziWzApZCAqlwOt3xK3L0B02VjEsDFZg4Fniy76TsTLKgtnjqlG"

access_token = "1587880604-1tjWpdETzVE4fPALCGeNs6O2oHi4y8ShwIsDQSl"
access_token_secret = "wJHBahm2y3KnTXuuj2JX18GAolaHVMnLKZ7Ygc0LxnQMH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

'''
twitter = Twython(consumer_key, consumer_secret, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(consumer_key, access_token=ACCESS_TOKEN)
'''
training_data = gttd.get_training_data()

def download_tweets():
    j = 0
    users = []
    #cleaned_tweets = []
    hotspot_list = []
    area = []
    '''
    print("Tweets downloading has started !!")
    maxTweets = 1000  # Some arbitrary large number
    tweetsPerQry = 100  # this is the max the API permits

    # If results from a specific ID onwards are reqd, set since_id to that ID.
    # else default to no lower limit, go as far back as API allows
    sinceId = None

    # If results only below a specific ID are, set max_id to that ID.
    # else default to no upper limit, start from the most recent tweet matching the search query.
    max_id = -1

    tweets = []
    tweetCount = 0
    '''
    f = open("hotspot_list.csv","r")
    for row in f:
        hotspot_list.append(row.split(",")[0])
        area.append(row.split(",")[1])
    f.close()

    keyword_list = []
    f = open("keyword_list.txt","r")
    for word in f:
        keyword_list.append(word.split("\r")[0])
    f.close()

    for i in range(len(hotspot_list)):
        city_search = api.geo_search(query=hotspot_list[i], granularity="city")
        geocode = city_search[0].centroid
        r = sqrt(float(area[i])/3.14)
        r = r - ((r/10)+1)
        r = int(r)

        for hashtag in keyword_list:
            #tweets = []
            print hashtag,hotspot_list[i]
            #while True:

            with open("users.json", 'a') as f:
                '''
                while tweetCount < maxTweets:
                    try:
                        if (max_id <= 0):
                            if (not sinceId):
                                new_tweets = api.search(q=hashtag, count=tweetsPerQry, geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + str(r) + "mi")
                            else:
                                new_tweets = api.search(q=hashtag, count=tweetsPerQry, geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + str(r) + "mi", since_id=sinceId)
                        else:
                            if (not sinceId):
                                new_tweets = api.search(q=hashtag, count=tweetsPerQry, geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + str(r) + "mi",max_id=str(max_id - 1))
                            else:
                                new_tweets = api.search(q=hashtag, count=tweetsPerQry, geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + str(r) + "mi", max_id=str(max_id - 1), since_id=sinceId)

                        if not new_tweets:
                            print("No more tweets found")
                            break

                        for tweet in new_tweets:
                '''

                        #f = open('lot_of_tweets.csv', 'a')
                for tweet in tweepy.Cursor(api.search,q=word,geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + str(r)+"mi",lang='en').items():
                        #for status in tweepy.Cursor(api.search,q='',lang='en',since_id=None).items():

                    j += 1
                    if check(tweet.author._json['followers_count'], tweet.author._json['friends_count']):
                        #tweets.append({'user_name':tweet.author._json['screen_name'],'user_mention':tweet.entities['user_mentions'], 'profile_image':tweet.author._json['profile_image_url_https']})
                        #users.append({'user_name':tweet.author._json['screen_name'],'user_mention':tweet.entities['user_mentions'],'name':tweet.author._json['name']})

                        cleaned_tweet = clean(tweet.text.encode('ascii','ignore'))
                        if True:
                        #if cleaned_tweet not in cleaned_tweets:
                            if True:
                            #if len(cleaned_tweet.split(" ")) > 3:

                                #print cleaned_tweet         # helps see the progress (although slows down the actual process a bit)
                                classifier = get_classifier_MNB(training_data)      # if the classifier hasn't been trained before
                                fs = get_feature_set(cleaned_tweet)

                                if classifier.classify(fs):
                                    users.append({'user_name':tweet.author._json['screen_name'],'user_mention':tweet.entities['user_mentions'],'name':tweet.author._json['name']})
                                    #f.write(cleaned_tweet+"\n")
                                    #cleaned_tweets.append(cleaned_tweet)

                    if j > 3000:
                        break

                    if j%500 == 0:
                        print j,"tweets processed. Taking a 100 seconds break. -_-"
                        time.sleep(100)
                        '''
                        tweetCount += len(new_tweets)
                        print("Downloaded {0} tweets".format(tweetCount))
                        max_id = new_tweets[-1].id
                #f.close()
                #break
                    except tweepy.TweepError as e:
                        # Just exit if any error
                        print("some error : " + str(e))
                        break
                        '''
                json.dump(users,f)

            #break
        #break

'''
tweets2 = []
try:
    tweets = twitter.search(q = "fitness", geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + radius, lang = 'en')['statuses']
except TwythonError as e:
    print e
print len(tweets)
while len(tweets) != 0:
    try:
        tweets = twitter.search(q = "fitness", geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + radius, lang = 'en', max_id = tweets[len(tweets)-1]['id']-1)['statuses']
    except TwythonError as e:
            print e
    for tweet in tweets:
        tweets2.append(tweet['text'])
print len(tweets2)

'''
download_tweets()

