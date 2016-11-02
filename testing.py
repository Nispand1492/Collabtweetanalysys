# import tweepy
# from tweepy import Stream
# from tweepy import OAuthHandler
# import time
# import json
# import datetime
# import pickle
# ckey = 'Fzu9VAcWENP2S9l6CSKmYDFFq'
# csecret = 'ZnsmakcD1UCd7LxVYeJuUoSk8Rp8hvI2sZHMo9FMDxmdcvc1Ai'
# atoken = '133215194-QPRP9T4a70fPPnwFu4HE2rB8PJr3ysjiyFY6R3iZ'
# asecret = 'hyTIEpveHllM1m8gNobt4Fxw59p3AWptSUZQyLVOuPq9l'
#
# auth = OAuthHandler(ckey, csecret)
# auth.set_access_token(atoken, asecret)
#
# api = tweepy.API(auth)
# user = '@the_rush_tea'
# id= 792855903011733504
# rpl_id = 788907505178988544
# temp_id = id
# ids = []
# res = api.get_status(id)
# print (res._json['created_at'])
# print(len(res))
# for tweet in res:
#      print(tweet._json)
#      print(tweet.user.screen_name + " --> " + tweet.text)

# obj  = pickle.load( open( "Output.p", "rb" ) )
# print(obj)
# pickle.dump(obj,open("Output1.p","wb"),2)
# time_str = "Tue Jan 12 21:33:28 +0000 2010"
# t = datetime.datetime.strptime(time_str,"%a %b %d %H:%M:%S %z %Y")
# print(t+datetime.timedelta(minutes = 10))
#!/usr/bin/env python
import re

text = u'This dog \U0001f602'
print(text) # with emoji

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
print(emoji_pattern.sub(r'', text)) # no emoji
