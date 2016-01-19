import tweepy
import retrive_twitter_info

class Tw():
	def __init__(self, keys): 
		self.keys = keys

	def login(self, key):
		# get twitter user
	  return retrive_twitter_info.GetTwitterInfo(
	    key["consumer_key"], 
	    key["consumer_secret"], 
	    key["access_token"], 
	    key["access_token_secret"], 
	    key["screen_name"]
	  )

	def select_account(self):
		accounts = options = []
		for i, key in enumerate(self.keys):
			accounts.append(key["screen_name"])
			options.append( key["screen_name"] + "[" + str(i + 1) + "]" )   

		i = int(input("Which twitter account do you want to use? " + ', '.join(options) + ": "))
		print("The user is " + accounts[i-1])

		return self.login( self.keys[i-1] )

	def get_keys(self):
		return self.keys