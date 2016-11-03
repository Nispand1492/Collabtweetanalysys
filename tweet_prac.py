import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import time
import json
from tweepy.streaming import StreamListener
import datetime
from tweet_class import Tweet
import pickle
from collections import deque
def get_tweet(user,id,maxid):
    res = api.search(q=user,count=100,since_id=id,max_id = maxid)
    return res

def format_dat(time_str):
    t = datetime.datetime.strptime(time_str,"%a %b %d %H:%M:%S %z %Y")
    return t

def get_all_child(root):
    f = open("Outputtest.txt",'a')
    flag = True
    id = root.tweet_data['tweet_id']
    cnt = 0
    max_id = 1
    old_max = 1
    tweet_list = []
    ids = []
    user = '@' + str(root.get_username())
    while flag:
        if(cnt == 179):
             print("Max request level reached..Waiting for 15 minutes")
             print("Wait Over...Starting again...")
             cnt = 0
        if(max_id == 1):
                cnt = cnt + 1
                print("Sending request number :"+str(cnt))
                time.sleep(5)
                res = api.search(q=user,count=100 ,since_id=id)
                print("size of response:"+str(len(res)))
                if(len(res)== 0):
                    flag = False
                    break
        elif max_id <= id:
            flag = False
        else:
                cnt = cnt +  1
                time.sleep(5)
                print("Sending request number :"+str(cnt))
                res = get_tweet(user,id,max_id)
                print("size of response:"+str(len(res)))
                if(len(res) == 0):
                    flag = False
                    break

        for tweet in res:
            if(tweet.id in ids):
                continue

            ids.append(tweet.id)
            if tweet.in_reply_to_status_id_str == str(id):
                tweet_data = {'tweet_id':tweet.id,'tweet_text':tweet.text,'author_id':tweet.user.screen_name,'replied_to_user':tweet.in_reply_to_screen_name,'reply_to_tweet':tweet.in_reply_to_status_id_str}
                new_child = Tweet(tweet_data)
                f.write(json.dumps(tweet_data))
                tweet_list.append(new_child)
                print(tweet.user.screen_name + " --> " +tweet.text)
        old_max = max_id
        max_id = min(ids)
        if old_max == max_id:
            flag = False
            ids = []
    root.add_child(tweet_list)
    f.close()
    return "success"
#Credentials
#consumer key,consumer secret key,access token,access secret
ckey = ''
csecret = ''
atoken = ''
asecret = ''
queue = deque([])
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

#Add User Name in place of of the tweet you want to analyse Below.
user = '@Being_Humor'
#Add tweet id of the tweet you want to analyse Below.
id= 794045925756981248
temp_id = id
ids = []
data = api.get_status(id)
tweet_data = {'tweet_id':id,'tweet_text':data.text,'author_id':data.user.screen_name,'replied_to_user':data.in_reply_to_screen_name,'reply_to_tweet':data.in_reply_to_status_id_str}
root = Tweet(tweet_data)
status = get_all_child(root)
queue.append(root)
while(queue):
    next = queue.popleft()
    childs = next.get_child()
    for child in childs:
        get_all_child(child)
        queue.append(child)
    next.visited = True

pickle.dump(root,open("Outputtest.p","wb"))
tweet_list = ['']


