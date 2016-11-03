# import tweepy
# from tweepy import Stream
# from tweepy import OAuthHandler
# import time
# import json
# import datetime
import pickle

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

obj  = pickle.load( open( "Outputtest.p", "rb" ) )
print("done")
 #print(obj)
# pickle.dump(obj,open("Output1.p","wb"),2)
# time_str = "Tue Jan 12 21:33:28 +0000 2010"
# t = datetime.datetime.strptime(time_str,"%a %b %d %H:%M:%S %z %Y")
# print(t+datetime.timedelta(minutes = 10))
