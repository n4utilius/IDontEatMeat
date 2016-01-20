import tweepy
import retrive_twitter_info
from keys2 import keys
import datetime, time


class Tw():
	
	def __init__(self): 
		self.keys = keys
		self.user = [] # current user
		self.screen_name = '' # current username
		self.api = [] # current user api

	def login(self, key):
		# get twitter user
	  self.user = retrive_twitter_info.GetTwitterInfo(
	    key["consumer_key"], 
	    key["consumer_secret"], 
	    key["access_token"], 
	    key["access_token_secret"], 
	    key["screen_name"]
	  )
	  
	  auth = tweepy.OAuthHandler( key["consumer_key"], key["consumer_secret"] )
	  auth.set_access_token( key["access_token"], key["access_token_secret"] )

	  self.screen_name = key["screen_name"]
	  self.api = tweepy.API(auth)

	  return self.user 

	def select_account(self):
		accounts = options = []
		for i, key in enumerate(self.keys):
			accounts.append(key["screen_name"])
			options.append( key["screen_name"] + "[" + str(i + 1) + "]" )   

		i = int(input("Which twitter account do you want to use? " + ', '.join(options) + ": "))
		print("The user is " + accounts[i-1])

		return (self.login( self.keys[i-1] ), i - 1)

	def get_keys(self):
		return self.keys

	def search_tweets(self, query, language, max_tweets):
		return [ status for status in tweepy.Cursor(self.user.api.search, q=query, lang=language).items(max_tweets)]

	def get_api(self): 
		return self.api

	def getFollowers(self):
		ids = []
		for page in tweepy.Cursor(self.api.followers_ids, screen_name = self.screen_name ).pages():
			ids.extend(page)
			time.sleep(60)
		return ids, str(self.screen_name)

	def get_screen_name(self):
		return self.screen_name