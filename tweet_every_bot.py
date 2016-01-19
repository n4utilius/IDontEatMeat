import tweepy
import retrive_twitter_info
from keys2 import keys

def tw_login(key):
  user = retrive_twitter_info.GetTwitterInfo(
    key["consumer_key"], 
    key["consumer_secret"], 
    key["access_token"], 
    key["access_token_secret"], 
    key["screen_name"]
  )
  return user

def send_tweet(tweet): 
  try:
    publish = raw_input("Publish? [Y]es  to publish [N]o to pass or [E]xit to exit ")
   
    if publish.lower() == 'y':
      for key in keys: tw_login(key).api.update_status(status=str(tweet))
    
    elif publish.lower() == 'n': pass
    
    elif publish.lower() == 'e': pass

  except IndexError:
    pass

tweet = raw_input("What do you want to tweet every bot ?")
send_tweet(tweet)