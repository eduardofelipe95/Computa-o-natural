from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import json
import pymongo
from pymongo import MongoClient

ckey = '5cNHq4vqqO1HtdMxVg6awaaaa'
csecret = 'VLikHoKhFtOBM8MZ37bekYJXC9nO5uk7huYY3uZKVSZOcTJDMH'
atoken = '907596718413316098-cRSgOH3Aw3XRjxogEXtAJOkKvoFJ13Y'
asecret = 'XSaImTWTgBJIEIkwFZyn4qLuPsJJVXhm2U1bqszB9Hwl8'

client = MongoClient('localhost', 27017)
db = client.twitter
collection = db.tweets



class StdOutListener(StreamListener):

    def on_data(self, data):
    		
	        print ('\n')
	        d = json.loads(data)
	        print (data)
	        collection.insert_one(d)
	        #saveFile = open('twitDB.CSV', 'a')
	        #saveFile.write(data)
	        #saveFile.write('\n')
	        #saveFile.close()
	    


    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    stream = Stream(auth, l)

    stream.filter(track=['brasil', 'flamengo'])