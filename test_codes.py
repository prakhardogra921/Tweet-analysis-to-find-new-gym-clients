__author__ = 'prakhardogra'
'''
from classify import get_classifier_MNB
from ef import get_feature_list
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
import pickle
'''
#from fs import get_feature_set
hotspot_list = []
area = []
import tweepy
from twython import Twython, TwythonError

consumer_key = "RGVO3CTujE60TW5IQy1JwmyxF"
consumer_secret = "ziWzApZCAqlwOt3xK3L0B02VjEsDFZg4Fniy76TsTLKgtnjqlG"

access_token = "1587880604-1tjWpdETzVE4fPALCGeNs6O2oHi4y8ShwIsDQSl"
access_token_secret = "wJHBahm2y3KnTXuuj2JX18GAolaHVMnLKZ7Ygc0LxnQMH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

twitter = Twython(consumer_key, consumer_secret, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(consumer_key, access_token=ACCESS_TOKEN)

'''
f = open("hotspot_list.csv","r")
for row in f:
    hotspot_list.append(row.split(",")[0])
    area.append(row.split(",")[1])
    print row
print hotspot_list, area


keyword_list = []
f = open("keyword_list.txt","r")
print f
for word in f:
    keyword_list.append(word.split("\r")[0])
print keyword_list
'''
'''
string = "went to the gym for hours in the morning and then went to the stadium to do some cardio and work on legs im pooped"
f = open("lot_of_tweets.csv","r")
list = []
classifier = get_classifier_MNB(list)
for row in f:
    fs = get_feature_set(row)
    print classifier.classify(fs)
'''
#print list

      # giving better results
#print classifier
#a = dict()


#print classifier.classify(get_feature_list(list))

#jdjdjd

import json

#from download_tweets import download_tweets

#download_tweets()

with open("tweets.json", 'r') as f:
    users = json.load(f)
#print users
all_users = []
all_names = []
for user in users:
    if user['user_name'] not in all_users:
        all_users.append(user['user_name'])
        #all_names.append(user['name'])
    if user['user_mention']:
        mentioned_user = user['user_mention'][0]['screen_name']
        if mentioned_user not in all_users:
            all_users.append(mentioned_user)
            #all_names.append(user['user_mention']['name'])

f = open('users.csv','a')
for i in range(len(all_users)):
    #row = all_users[i] + "," + all_names[i] + "\n"
    row = all_users[i]+"\n"
    f.write(row)
f.close()


city_search = api.geo_search(query='Atlanta', granularity="city")
geocode = city_search[0].centroid
'''
for tweet in tweepy.Cursor(api.search,q='fit',geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + "50mi",lang='en').items():
    print tweet._json['retweeted']
    break
'''
'''
tweets2 = []
i = 0
try:
    tweets = tweepy.Cursor(api.search,q='fit',geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + "50mi",lang='en').items()
except TwythonError as e:
    print e
for tweet in tweets:
    i += 1
print i
#print len(tweets)
while len(i) != 0:
    try:
        tweets = tweepy.Cursor(api.search,q='fit',geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + "50mi",lang='en', max_id = tweets[i-1]['id']-1).items()
    except TwythonError as e:
            print e
    for tweet in tweets:
        tweets2.append(tweet.text)
print len(tweets2)
'''
'''
try:
    tweets = twitter.search(q = "fitness", geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + "50mi", lang = 'en')['statuses']
except TwythonError as e:
    print e
print len(tweets)
while len(tweets) != 0:
    try:
        tweets = twitter.search(q = "fitness", geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + "50mi", lang = 'en', max_id = tweets[len(tweets)-1]['id']-1)['statuses']
    except TwythonError as e:
            print e
    for tweet in tweets:
        tweets2.append(tweet['text'])
print len(tweets2)
'''

import tweepy

# Twitter API credentials

consumer_key = "RGVO3CTujE60TW5IQy1JwmyxF"
consumer_secret = "ziWzApZCAqlwOt3xK3L0B02VjEsDFZg4Fniy76TsTLKgtnjqlG"
access_key = "1587880604-1tjWpdETzVE4fPALCGeNs6O2oHi4y8ShwIsDQSl"
access_secret = "wJHBahm2y3KnTXuuj2JX18GAolaHVMnLKZ7Ygc0LxnQMH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)


def get_all_hash(name):
    hashtag = name
    api = tweepy.API(auth)
    print("Tweets downloading has started !!")
    maxTweets = 10000  # Some arbitrary large number
    tweetsPerQry = 100  # this is the max the API permits
    #fName = 'HDFCTweets.txt'  # We'll store the tweets in a text file.

    # If results from a specific ID onwards are reqd, set since_id to that ID.
    # else default to no lower limit, go as far back as API allows
    sinceId = None

    # If results only below a specific ID are, set max_id to that ID.
    # else default to no upper limit, start from the most recent tweet matching the search query.
    max_id = -1

    tweets = []
    tweetCount = 0
    print("Downloading max {0} tweets".format(maxTweets))
    #file_folder = ownModule.createFileFolder()
    with open("some_tweets.csv", 'w') as f:
        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = api.search(q=hashtag, count=tweetsPerQry, geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + "50mi")
                    else:
                        new_tweets = api.search(q=hashtag, count=tweetsPerQry, geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + "50mi", since_id=sinceId)
                else:
                    if (not sinceId):
                        new_tweets = api.search(q=hashtag, count=tweetsPerQry, geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + "50mi",max_id=str(max_id - 1))
                    else:
                        new_tweets = api.search(q=hashtag, count=tweetsPerQry, geocode=str(geocode[1]) + ',' + str(geocode[0]) + ',' + "50mi", max_id=str(max_id - 1), since_id=sinceId)
                if not new_tweets:
                    print("No more tweets found")
                    break
                for tweet in new_tweets:
                    print tweet
                    break
                    tweets.append(tweet.text)
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break

    return tweets
get_all_hash("fit")
'''
#all_users = []
#all_names = []
f = open("users.csv","r+")
for row in f:
    all_users.append(row.split("\n")[0])
f.close()

new_users = []
new_names = []
for i in range(len(all_users)):
    if all_users[i] not in new_users:
        new_users.append(all_users[i])
        #new_names.append(all_names[i])
f = open("users.csv","w+")
for i in range(len(new_users)):
    #row = all_users[i] + "," + all_names[i] + "\n"
    row = new_users[i]+"\n"
    f.write(row)
f.close()
'''