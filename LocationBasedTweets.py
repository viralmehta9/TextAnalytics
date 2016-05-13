# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 09:01:31 2016

@author: viral
"""

from TwitterSearch import TwitterSearchOrder
from TwitterSearch import TwitterSearch
from TwitterSearch import TwitterSearchException

# First, let's grab a user's timeline. Use the
# 'screen_name' parameter with a Twitter user name.


try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_key
    tso.set_keywords(['swamy39']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information
    
    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'V3vtYV8UdvoQPfk0hkoA3hEI1',
        consumer_secret = 'N9Gy4HQpn598ENjRSI71JCKUsh7ivG73YWR7kvwaBhzWHB8zmT',
        access_token = '893216012-rXzWnM1PWf89YHF7wu8xrhMooBkDeEHhjW6AcMXq',
        access_token_secret = 'ko7P2wsDwMiYZ24iyWdcQet5RJF8TgqCBERaYjKLEtjYo'
     )

    MAX_LIMIT = 50
    count =0    
    # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        count += 1        
        if count == MAX_LIMIT:
            break
except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)








'''
from twython import Twython
#from collections import Counter

#import string

api_key = "V3vtYV8UdvoQPfk0hkoA3hEI1"
api_secret = "N9Gy4HQpn598ENjRSI71JCKUsh7ivG73YWR7kvwaBhzWHB8zmT"
access_token = "893216012-rXzWnM1PWf89YHF7wu8xrhMooBkDeEHhjW6AcMXq"
token_secret = "ko7P2wsDwMiYZ24iyWdcQet5RJF8TgqCBERaYjKLEtjYo"
api = Twython(api_key, api_secret, access_token, token_secret)

def get_tweets(twython_object, query, n):
    result_generator = twython_object.cursor(twython_object.search, q = query)
    return result_generator
    
rg = get_tweets(api, '#trump',1)
MAX_LIMIT = 1 #limit tweets to 10
print (type(rg))
tweets = []
count = 0
for r in rg:
    #print(r['text'])
    tweets.append(r)
    count += 1
    #print(r)
    print(r['user']['location'])
    if count == MAX_LIMIT:
        break
    #print(r)
    
        
tweetSentScore = []
wordList = []
documentList = []
for tweet in tweets:
    txt = tweet['text']
    #txt = parse(txt)
    documentList.append(txt)
    words = txt.split()
    for item in words:
        wordList.append(item)
    
'''  