from tw import Tw

def send_tweet(tweet): 
  try:
    publish = raw_input("Publish? [Y]es  to publish [N]o to pass or [E]xit to exit ")
    
    if publish.lower() == 'y':
      t = Tw()
      for key in t.get_keys(): t.login(key).api.update_status(status=str(tweet))
    
    elif publish.lower() == 'n': pass
    
    elif publish.lower() == 'e': pass

  except IndexError:
    pass

tweet = raw_input("What do you want to tweet every bot? ")
send_tweet(tweet)