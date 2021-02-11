import requests
import urllib.parse
import json

def getToken1():
    request = requests.get("https://abs.twimg.com/responsive-web/client-web/main.a8574df5.js")
    text_block = request.text
    action_refresh_section = text_block[text_block.index('i="ACTION_REFRESH"'):]
    sections = action_refresh_section.split(',')
    for section in sections:
        if section[0:2]=='a=':
            token = urllib.parse.unquote(section[3:-1])
            break
    return(token)

def getToken2(token1):
    request = requests.post("https://api.twitter.com/1.1/guest/activate.json", headers={"Authorization":'Bearer '+token1})
    token = request.json()['guest_token']
    return(token)

def getUserRestID(screen_name, token1, token2):
    variables = {'variables':json.dumps({'screen_name':screen_name,'withHighlitedLabel':True})}
    headers = {"Authorization":'Bearer '+token1,
               "x-guest-token":token2}
    url = """https://api.twitter.com/graphql/4S2ihIKfF3xhp-ENxvUAfQ/UserByScreenName?variables=%7B%22screen_name%22%3A%22"""+screen_name+"""%22%2C%22withHighlightedLabel%22%3Atrue%7D"""
    request = requests.get(url, headers=headers )
    return(request.json()['data']['user']['rest_id'])

def getUserTweets(screen_name, number_of_tweets):
    token1       = getToken1()
    token2       = getToken2(token1)
    user_rest_id = getUserRestID(screen_name, token1, token2)
    url = "https://api.twitter.com/2/timeline/profile/"+user_rest_id+".json"
    headers = {"Authorization":'Bearer '+token1,
               "x-guest-token":token2}
    params  = {"tweet_mode":"extended",
               "simple_quoted_tweet":True,
               "include_tweet_replies":True,
               "userId":user_rest_id,
               "count":number_of_tweets}
    request = requests.get(url, params=params, headers = headers)
    return(request.json()['globalObjects']['tweets'])

#Get dem tweets
tweets = getUserTweets('DalaiLama',2000)
#Chop dem tweets
tweet_texts = []
for tweet_id, tweet_data in tweets.items():
    tweet_text = tweet_data['full_text']
    #Only add tweet if it's not a hyperlink
    if ("/" not in tweet_text) and ('=' not in tweet_text):
        tweet_texts.append(tweet_text)
long_string = ' '.join( tweet_texts )
#Filter dem tweets
filtered_string="".join([character for character in long_string if ord(character) < 128])
#Save dem tweets
with open('text_dumps/dalai_lama.txt', 'w+') as f:
    f.write(filtered_string)

