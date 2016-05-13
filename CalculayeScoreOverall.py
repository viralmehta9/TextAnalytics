from anew_module import anew
def read_tweets(name):
    in_file = open("C:\\UTA Courses\\spring\\Data Science 5378\\textminingproject\\tweets\\text\\"+name+".csv", "r")
    tweets_list = in_file.read().splitlines()
    in_file.close()
    return tweets_list
    
# a file called afinity
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

# read lexicon words
positive_words_list=[]
negative_words_list=[]    
posfile = open("C:\\UTA Courses\\spring\\Data Science 5378\\textminingproject\\lexicon\\positive.csv","r")
negfile = open("C:\\UTA Courses\spring\\Data Science 5378\\textminingproject\\lexicon\\negative.csv","r")
positive_words_list=posfile.read().splitlines()
negative_words_list=negfile.read().splitlines()
positive_words_set=set(positive_words_list)
negative_words_set=set(negative_words_list)
posfile.close()
negfile.close()

def  compute_sentiment_score(wordsList):
    posscore = 0
    negscore = 0
    keys = d.keys()
    for word in wordsList:
        if word in keys:
            if int(d[word]) >= 0:
                posscore += int(d[word])
            else:
                negscore += int(d[word])
    return (posscore,negscore)

def compute_lexicon_score(wordsList):
    posscore = 0
    negscore = 0
    for word in wordsList:
        if word in positive_words_set:
            posscore += 1
        elif word in negative_words_set:
            negscore += 1            
    return (posscore,negscore) 
    
def  compute_sentiment_score_byAnew(wordsList):
    arousalScore = 0.0
    valenceScore = 0.0
    for word in wordsList:
        if anew.exist(word):
            arousalScore += anew.arousal(word)
            valenceScore += anew.valence(word)
    return (arousalScore,valenceScore)




def get_sentiment(tweets,name):
    tweetSentPosScore = []
    tweetSentNegScore = []
    lexposscore = []
    lexnegscore = []
    arousscore= []
    valencscore=[]
    
    for tweet in tweets:
        words = tweet.split()
        scoretuple=compute_sentiment_score(words)
        lextuple=compute_lexicon_score(words)
        anewtuple=compute_sentiment_score_byAnew(words)
        tweetSentPosScore.append(scoretuple[0])
        tweetSentNegScore.append(scoretuple[1])
        lexposscore.append(lextuple[0])
        lexnegscore.append(lextuple[1])
        arousscore.append(anewtuple[0])
        valencscore.append(anewtuple[1])
    print("The positive sentiment score for "+ name + " is: ")
    print("Affinity:"+str(sum(tweetSentPosScore)))
    print("lexicon:"+str(sum(lexposscore)))
    print("The Negative sentiment score for "+ name + " is: ")
    print("Affinity:"+str(sum(tweetSentNegScore)))
    print("lexicon:"+str(sum(lexnegscore)))
    print("overall sentiment is :")
    print("Affinity:"+str(sum(tweetSentPosScore)+sum(tweetSentNegScore)))
    print("lexicon:"+str(sum(lexposscore)-sum(lexnegscore)))
    print("ANEW Arousal score:"+str(sum(arousscore)))
    print("ANEW valence score:"+str(sum(valencscore)))


    
trumptweets=read_tweets("trumplist")
clintontweets=read_tweets("clintonlist")
sandtweets=read_tweets("sandlist")
cruztweets=read_tweets("cruzlist")

get_sentiment(trumptweets,"Trump")
get_sentiment(clintontweets,"Clinton")
get_sentiment(sandtweets,"Sanders")
get_sentiment(cruztweets,"Cruz")

    


