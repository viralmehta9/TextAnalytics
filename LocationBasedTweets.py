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
    tso.set_keywords(['trump']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False) # and don't give us all those entity information
    
    # it's about time to create a TwitterSearch object with our secret tokens
    # tokens are modified and dummy values are shown.
    ts = TwitterSearch(
        consumer_key = 'V3vV8UdvoQPfk0hkoA3hEI1',
        consumer_secret = 'N9Gy4HQpn698ENjHAF71JCKUsh7egA73Y7H3kvwaHwfswzmT',
        access_token = '89321hMoo60-rXz1PWf89YHxrBkDeEF8HhjcMXq',
        access_token_secret = 'koF8gq7wMiYZ24iydcQetJF8TgqCBERaKLEtjYo'

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
    
    
    
    
