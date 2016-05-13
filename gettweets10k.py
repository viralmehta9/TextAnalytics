import pickle
import re
from twython import Twython
import nltk
api_key = "kuKhjJMswByMa39wmREaGjPBj"
api_secret = "Td7SawQIpmRm3CdWKLerNCWANtIkVSr5Rb6WnNNeQ5ubewIUqx"
access_token = "148241515-aaZyAaW38dlg1aMHxCgTADydzG5RwaSJDHI9JbUZ"
token_secret = "Yfo6TNQY1AQK9V8cGbaryDraniKyWMnrkHDO7qyAqd0or" 
#api = Twython(api_key, api_secret, access_token, token_secret,oauth_version=2)
api = Twython(api_key, api_secret,oauth_version=2)
ACCESS_TOKEN = api.obtain_access_token()
api = Twython(api_key, access_token=ACCESS_TOKEN)
clintonlist=[]
trumplist=[]
sandlist=[]
cruzlist=[]

def get_tweets_list(twython_object, query, MAX_LIMIT):
    result_generator = twython_object.cursor(twython_object.search, q = query, count=100, lang='en')
    #twython_object.cursor(twython_object.search, q = query, count=100, Geolocalization = “37.781157,-122.398720,1mi”)
    tweets = []
    count = 0
    for r in result_generator:
        tweets.append(r)
        count += 1
        if count == MAX_LIMIT:
            break
    return tweets
clintonlist = get_tweets_list(api, '#Hillary', 10000 )
trumplist = get_tweets_list(api, '#Trump', 10000 )
sandlist = get_tweets_list(api, '#Sanders', 10000 )
cruzlist = get_tweets_list(api, '#Cruz', 10000 )
stopwords = nltk.corpus.stopwords.words("english")
customlist = ['rt','https','http']
stopwords=stopwords+customlist
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))',' ',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+',' ',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    #final cleanup
    validLetters = "abcdefghijklmnopqrstuvwxyz "
    tweet = ''.join([char for char in tweet if char in validLetters])
    words = tweet.split()
    tweetsWithoutStopWords = [w for w in words if w not in stopwords]
    tweet = ' '.join(tweetsWithoutStopWords)
    return tweet
#end

def write_tweets_file(my_list,name):
    out_file = open("C:\\UTA Courses\\spring\\Data Science 5378\\textminingproject\\tweets\\"+name+".csv","wb")
    pickle.dump(my_list, out_file)
    out_file.close()
def writereadabletweets(my_list,name):
    out_file = open("C:\\UTA Courses\\spring\\Data Science 5378\\textminingproject\\tweets\\text\\"+name+".csv","w")
    for tweet in  my_list:
        out_file.write(processTweet(tweet['text'])+'\n')
    out_file.close()
#    
#    in_file = open("C:\\UTA Courses\\spring\\Data Science 5378\\textminingproject\\tweets\\"+name+".csv", "rb")
#    tweets_list = pickle.load(in_file)
#    in_file.close()
#    return tweets_list
#
trumptweets=write_tweets_file(trumplist,"trumplist")
clintontweets=write_tweets_file(clintonlist,"clintonlist")
sandtweets=write_tweets_file(sandlist,"sandlist")
cruztweets=write_tweets_file(cruzlist,"cruzlist")

writereadabletweets(trumplist,"trumplist")
writereadabletweets(clintonlist,"clintonlist")
writereadabletweets(sandlist,"sandlist")
writereadabletweets(cruzlist,"cruzlist")

    