# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 16:57:52 2016

@author: viral
"""
# Creating dictionary of location and their coordinates.
import ast
import operator
from anew_module import anew
import pandas as pd

locationDictionary = {}
with open('C:\\UTA Courses\\spring\\Data Science 5378\\textminingproject\\stateLocationDictionary.txt','r') as inf:
    locationDictionary = ast.literal_eval(inf.read())
    #print(locationDictionary)
inf.close()

locationDictionary = sorted(locationDictionary.items(), key= operator.itemgetter(0))
# End

#Creating a list of only locations
stateList = []
for item in locationDictionary:
    stateList.append(item[0])
# End
    
# For AFFIN
#Read AFINN file and store it in a dictionary
d = {}
inFile = open("C:\\UTA Courses\\spring\\Data Science 5378\\textminingproject\\AFIMM.txt")
for line in inFile:
    line = line.strip()
    elements = line.split()
    if len(elements) > 2:
        d[' '.join(elements[:-1])] = elements[-1]
    else:
        d[elements[0]] = elements[1]
inFile.close()

AffinScoreStateWiseFortrump = {}

AffinFinalScoreStateWiseFortrump ={}
AffinFinalScoreStateWiseForCruz = {}
AffinFinalScoreStateWiseForHillary = {}
AffinFinalScoreStateWiseForSander = {}

LexiconFinalScoreStateWiseFortrump ={}
LexiconFinalScoreStateWiseForCruz={}
LexiconFinalScoreStateWiseForHillary={}
LexiconFinalScoreStateWiseForSander = {}

ArousalAnewFinalScoreStateWiseForTrump ={}
ValenceAnewFinalScoreStateWiseForTrump = {}
ArousalAnewFinalScoreStateWiseForCruz = {}
ValenceAnewFinalScoreStateWiseForCruz = {}
ArousalAnewFinalScoreStateWiseForHillary = {}
ValenceAnewFinalScoreStateWiseForHillary = {}
ArousalAnewFinalScoreStateWiseForSander = {}
ValenceAnewFinalScoreStateWiseForSander = {}

temperaryTweetsList = []
totaScore = 0

# Read Tweets Function
def read_tweets_Trump(item):
    in_file = open("C:\\UTA Courses\\spring\\Data Science 5378\\textminingproject\\TextTweets\\TrumpTweetsStateWise\\Trump-"+item+".txt", "r")   
    tweets_list = in_file.read().splitlines()
    in_file.close()
    return tweets_list
    
def read_tweets_Hillary(item):
    in_file = open("C:\\UTA Courses\\spring\\Data Science 5378\\textminingproject\\TextTweets\\HillarytweetsStateWise\\Hillary-"+item+".txt", "r")   
    tweets_list = in_file.read().splitlines()
    in_file.close()
    return tweets_list
    
def read_tweets_Cruz(item):
    in_file = open("C:\\UTA Courses\\spring\\Data Science 5378\\textminingproject\\TextTweets\\CruzTweetsStateWise\\Cruz-"+item+".txt", "r")   
    tweets_list = in_file.read().splitlines()
    in_file.close()
    return tweets_list
    
def read_tweets_Sander(item):
    in_file = open("C:\\UTA Courses\\spring\\Data Science 5378\\textminingproject\\TextTweets\\SanderTweetsStateWise\\Sander-"+item+".txt", "r")   
    tweets_list = in_file.read().splitlines()
    in_file.close()
    return tweets_list

def  compute_sentiment_AFINN(wordsList):
    posscore = 0
    negscore = 0
    keys = d.keys()
    for word in wordsList:
        for i in word:
            if i in keys:
                if int(d[i]) >= 0:
                    posscore += int(d[i])
                else:
                    negscore += int(d[i])
    return (posscore,negscore)
    
def compute_lexicon_score(wordsList):
    posscore = 0
    negscore = 0
    for word in wordsList:
        for i in word:
            if i in positive_words_set:
                posscore += 1
            elif i in negative_words_set:
                negscore += 1            
    return (posscore + negscore)

def  compute_sentiment_score_byAnew(wordsList):
    arousalScore = 0.0
    valenceScore = 0.0
    for word in wordsList:
        for i in word:
            if anew.exist(i):
                arousalScore += anew.arousal(i)
                valenceScore += anew.valence(i)
    return (arousalScore,valenceScore)

#For Trump --------------------------------
# Read tweets and calculate score for Trump
for item in stateList:
    words =[]
    temperaryTweetsList = read_tweets_Trump(item)
    for tweet in temperaryTweetsList:
        words.append(tweet.split())
    scoretuple=compute_sentiment_AFINN(words)
    totaScore += scoretuple[0] + scoretuple[1]
    AffinFinalScoreStateWiseFortrump[item] = totaScore

AffinFinalScoreStateWiseFortrump1 = sorted(AffinFinalScoreStateWiseFortrump.items(), key= operator.itemgetter(1))

print('\n For trump using AFFIN, the Top 5 states with positive sentiments are as ')
x = AffinFinalScoreStateWiseFortrump1[-5:]
x.reverse()
for item in x:
    print(item[0] + ' ' + str(item[1]))

print('\n For trump using AFFIN, the Top 5 states with negative sentiments are as ')
for item in AffinFinalScoreStateWiseFortrump1[:5]:
    print(item[0] + ' ' + str(item[1]))
    
# End for Trump------------------------------------------
   

# for Cruz----------------------------------------------

for item in stateList:
    words =[]
    temperaryTweetsList = read_tweets_Cruz(item)
    for tweet in temperaryTweetsList:
        words.append(tweet.split())
    scoretuple=compute_sentiment_AFINN(words)
    totaScore += scoretuple[0] + scoretuple[1]
    AffinFinalScoreStateWiseForCruz[item] = totaScore

    
AffinFinalScoreStateWiseForCruz = sorted(AffinFinalScoreStateWiseForCruz.items(), key= operator.itemgetter(1))

y = AffinFinalScoreStateWiseForCruz[-5:]
y.reverse()
print('\n For Cruz using AFFIN, the Top 5 states with positive sentiments are as ')
for item in y:
    print(item[0] + ' ' + str(item[1]))

print('\n For Cruz using AFFIN, the Top 5 states with negative sentiments are as ')
for item in AffinFinalScoreStateWiseForCruz[:5]:
    print(item[0] + ' ' + str(item[1]))
    
# End of Cruz ----------------------------------------
    
# for Hillary
    
for item in stateList:
    words =[]
    temperaryTweetsList = read_tweets_Hillary(item)
    for tweet in temperaryTweetsList:
        words.append(tweet.split())
    scoretuple=compute_sentiment_AFINN(words)
    totaScore += scoretuple[0] + scoretuple[1]
    AffinFinalScoreStateWiseForHillary[item] = totaScore
    
AffinFinalScoreStateWiseForHillary = sorted(AffinFinalScoreStateWiseForHillary.items(), key= operator.itemgetter(1))

a = AffinFinalScoreStateWiseForHillary[-5:]
a.reverse()
print('\n For Hillary using AFFIN, the Top 5 states with positive sentiments are as ')
for item in a:
    print(item[0] + ' ' + str(item[1]))

print('\n For Hillary using AFFIN, the Top 5 states with negative sentiments are as ')
for item in AffinFinalScoreStateWiseForHillary[:5]:
    print(item[0] + ' ' + str(item[1])) 
    
# End of Hillary ----------------------------------
    
# For Sander 

for item in stateList:
    words =[]
    temperaryTweetsList = read_tweets_Sander(item)
    for tweet in temperaryTweetsList:
        words.append(tweet.split())
    scoretuple=compute_sentiment_AFINN(words)
    totaScore += scoretuple[0] + scoretuple[1]
    AffinFinalScoreStateWiseForSander[item] = totaScore
    
AffinFinalScoreStateWiseForSander = sorted(AffinFinalScoreStateWiseForSander.items(), key= operator.itemgetter(1))

b = AffinFinalScoreStateWiseForSander[-5:]
b.reverse()
print('\n For Sander using AFFIN, the Top 5 states with positive sentiments are as ')
for item in b:
    print(item[0] + ' ' + str(item[1]))

print('\n For Sander using AFFIN, the Top 5 states with negative sentiments are as ')
for item in AffinFinalScoreStateWiseForSander[:5]:
    print(item[0] + ' ' + str(item[1]))   
# End of AFINN -------------------------------------------

# For Lexicon Positive and Negative Word
# Reading positive and negative words file and creating a list
posfile = open("C:\\UTA Courses\\spring\\Data Science 5378\\textminingproject\\lexicon\\positive.csv","r")
negfile = open("C:\\UTA Courses\spring\\Data Science 5378\\textminingproject\\lexicon\\negative.csv","r")
positive_words_list=posfile.read().splitlines()
negative_words_list=negfile.read().splitlines()
positive_words_set=set(positive_words_list)
negative_words_set=set(negative_words_list)

# For Trump

for item in stateList:
    words =[]
    temperaryTweetsList = read_tweets_Trump(item)
    for tweet in temperaryTweetsList:
        words.append(tweet.split())
    totalScore = compute_lexicon_score(words)
    LexiconFinalScoreStateWiseFortrump[item] = totalScore

LexiconFinalScoreStateWiseFortrump = sorted(LexiconFinalScoreStateWiseFortrump.items(), key= operator.itemgetter(1))

c = LexiconFinalScoreStateWiseFortrump[-5:]
c.reverse()
print('\n For trump lexicon, the Top 5 states with positive sentiments are as ')
for item in c:
    print(item[0] + ' ' + str(item[1]))

print('\n For trump lexicon, the Top 5 states with negative sentiments are as ')
for item in LexiconFinalScoreStateWiseFortrump[:5]:
    print(item[0] + ' ' + str(item[1]))
    
# End of Trump
 
  
# For Cruz

for item in stateList:
    words =[]
    temperaryTweetsList = read_tweets_Cruz(item)
    for tweet in temperaryTweetsList:
        words.append(tweet.split())
    totalScore = compute_lexicon_score(words)
    LexiconFinalScoreStateWiseForCruz[item] = totalScore

LexiconFinalScoreStateWiseForCruz = sorted(LexiconFinalScoreStateWiseForCruz.items(), key= operator.itemgetter(1))

d = LexiconFinalScoreStateWiseForCruz[-5:]
d.reverse()
print('\n For Cruz using lexicon, the Top 5 states with positive sentiments are as ')
for item in d:
    print(item[0] + ' ' + str(item[1]))

print('\n For Cruz using lexicon, the Top 5 states with negative sentiments are as ')
for item in LexiconFinalScoreStateWiseForCruz[:5]:
    print(item[0] + ' ' + str(item[1]))
    
# End of Cruz
    
# For Hillary
    
for item in stateList:
    words =[]
    temperaryTweetsList = read_tweets_Hillary(item)
    for tweet in temperaryTweetsList:
        words.append(tweet.split())
    totalScore = compute_lexicon_score(words)
    LexiconFinalScoreStateWiseForHillary[item] = totalScore

LexiconFinalScoreStateWiseForHillary = sorted(LexiconFinalScoreStateWiseForHillary.items(), key= operator.itemgetter(1))

e = LexiconFinalScoreStateWiseForHillary[-5:]
e.reverse()
print('\n For Hillary using lexicon, the Top 5 states with positive sentiments are as ')
for item in e:
    print(item[0] + ' ' + str(item[1]))

print('\n For Hillary using lexicon, the Top 5 states with negative sentiments are as ')
for item in LexiconFinalScoreStateWiseForHillary[:5]:
    print(item[0] + ' ' + str(item[1]))
    
# End of Hillary
    
# For Sander
 
for item in stateList:
    words =[]
    temperaryTweetsList = read_tweets_Sander(item)
    for tweet in temperaryTweetsList:
        words.append(tweet.split())
    totalScore = compute_lexicon_score(words)
    LexiconFinalScoreStateWiseForSander[item] = totalScore

LexiconFinalScoreStateWiseForSander = sorted(LexiconFinalScoreStateWiseForSander.items(), key= operator.itemgetter(1))

f = LexiconFinalScoreStateWiseForSander[-5:]
f.reverse()
print('\n For Sander using lexicon, the Top 5 states with positive sentiments are as ')
for item in f:
    print(item[0] + ' ' + str(item[1]))

print('\n For Sander using lexicon, the Top 5 states with negative sentiments are as ')
for item in LexiconFinalScoreStateWiseForSander[:5]:
    print(item[0] + ' ' + str(item[1]))   

# End of Sander

# End of Lexicon ----------------------------------------------


# For ANEW Modlue

# For Trump

for item in stateList:
    words =[]
    temperaryTweetsList = read_tweets_Trump(item)
    for tweet in temperaryTweetsList:
        words.append(tweet.split())
    totalScore = compute_sentiment_score_byAnew(words)
    ArousalAnewFinalScoreStateWiseForTrump[item] = totalScore[0]
    ValenceAnewFinalScoreStateWiseForTrump[item] = totalScore[1]

ArousalAnewFinalScoreStateWiseForTrump = sorted(ArousalAnewFinalScoreStateWiseForTrump.items(), key= operator.itemgetter(1))
ValenceAnewFinalScoreStateWiseForTrump = sorted(ValenceAnewFinalScoreStateWiseForTrump.items(), key= operator.itemgetter(1))

g = ArousalAnewFinalScoreStateWiseForTrump[-5:]
g.reverse()
print('\n Arousal Score  For trump using ANEW module, the Top 5 states are as ')
for item in g:
    print(item[0] + ' ' + str(item[1]))
    
h = ValenceAnewFinalScoreStateWiseForTrump[-5:]
h.reverse()   
print('\n Valence Score  For trump using ANEW module, the Top 5 states are as ')
for item in h:
    print(item[0] + ' ' + str(item[1]))

    
# End of Trump
    
# for Cruz
    
for item in stateList:
    words =[]
    temperaryTweetsList = read_tweets_Cruz(item)
    for tweet in temperaryTweetsList:
        words.append(tweet.split())
    totalScore = compute_sentiment_score_byAnew(words)
    ArousalAnewFinalScoreStateWiseForCruz[item] = totalScore[0]
    ValenceAnewFinalScoreStateWiseForCruz[item] = totalScore[1]

ArousalAnewFinalScoreStateWiseForCruz = sorted(ArousalAnewFinalScoreStateWiseForCruz.items(), key= operator.itemgetter(1))
ValenceAnewFinalScoreStateWiseForCruz = sorted(ValenceAnewFinalScoreStateWiseForCruz.items(), key= operator.itemgetter(1))

j = ArousalAnewFinalScoreStateWiseForCruz[-5:]
j.reverse()
print('\n Arousal Score  For Cruz using ANEW module, the Top 5 states are as ')
for item in j:
    print(item[0] + ' ' + str(item[1]))
  
k = ValenceAnewFinalScoreStateWiseForCruz[-5:]
k.reverse()  
print('\n Valence Score  For Cruz using ANEW module, the Top 5 states are as ')
for item in ValenceAnewFinalScoreStateWiseForCruz[-5:]:
    print(item[0] + ' ' + str(item[1])) 
    
# End of Cruz 
    
# For Hillary
    
for item in stateList:
    words =[]
    temperaryTweetsList = read_tweets_Hillary(item)
    for tweet in temperaryTweetsList:
        words.append(tweet.split())
    totalScore = compute_sentiment_score_byAnew(words)
    ArousalAnewFinalScoreStateWiseForHillary[item] = totalScore[0]
    ValenceAnewFinalScoreStateWiseForHillary[item] = totalScore[1]

ArousalAnewFinalScoreStateWiseForHillary = sorted(ArousalAnewFinalScoreStateWiseForHillary.items(), key= operator.itemgetter(1))
ValenceAnewFinalScoreStateWiseForHillary = sorted(ValenceAnewFinalScoreStateWiseForHillary.items(), key= operator.itemgetter(1))

l = ArousalAnewFinalScoreStateWiseForHillary[-5:]
l.reverse()
print('\n Arousal Score  For Hillary using ANEW module, the Top 5 states are as ')
for item in l:
    print(item[0] + ' ' + str(item[1]))

m = ValenceAnewFinalScoreStateWiseForHillary[-5:]
m.reverse()    
print('\n Valence Score  For Hillary using ANEW module, the Top 5 states are as ')
for item in m:
    print(item[0] + ' ' + str(item[1])) 
    
# End of Hillary
    
# For Sander
    
for item in stateList:
    words =[]
    temperaryTweetsList = read_tweets_Sander(item)
    for tweet in temperaryTweetsList:
        words.append(tweet.split())
    totalScore = compute_sentiment_score_byAnew(words)
    ArousalAnewFinalScoreStateWiseForSander[item] = totalScore[0]
    ValenceAnewFinalScoreStateWiseForSander[item] = totalScore[1]

ArousalAnewFinalScoreStateWiseForSander = sorted(ArousalAnewFinalScoreStateWiseForSander.items(), key= operator.itemgetter(1))
ValenceAnewFinalScoreStateWiseForSander = sorted(ValenceAnewFinalScoreStateWiseForSander.items(), key= operator.itemgetter(1))

n = ArousalAnewFinalScoreStateWiseForSander[-5:]
n.reverse()
print('\n Arousal Score  For Sander using ANEW module, the Top 5 states are as ')
for item in n:
    print(item[0] + ' ' + str(item[1]))

o = ValenceAnewFinalScoreStateWiseForSander[-5:]
o.reverse()   
print('\n Valence Score  For Sander using ANEW module, the Top 5 states are as ')
for item in o:
    print(item[0] + ' ' + str(item[1])) 

    

    
    



  




    
    
    
    


        
    
    



    

