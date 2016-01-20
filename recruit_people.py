from peewee import *
from create_recruited_database import Recruited,Tweets,Hashtag
from tw import Tw

class Recruit:
  def __init__(self, tw, db):
    self.tw = tw
    self.db = db

  def search_and_save_users(self):
    language = 'en'
    #use the lines below if you want to target another language besides english
    language = raw_input("Which language do you want to target 'es'espanish, 'en'english: ")
    language = language.lower()

    query = raw_input("Which words do you want to search? ")

    max_tweets = int(input("How many tweets do you want to retrieve? "))
    tweets = self.tw.search_tweets(query, language, max_tweets)

    list_user=[]
    list_hashtag=[]
    list_tweets =[]
    print('users found saved to the database: ')
    for elem in tweets:
      list_user.append({'user_id': elem.user.id, 'screen_name': elem.user.screen_name, 'description': elem.user.description})
      list_hashtag.append({'user_of_hashtag': elem.user.id, 'hashtag_text': query})
      list_tweets.append({'user_tweets': elem.user.id, 'tweet_message': elem.text, 'created_date': elem.created_at})

    for itemr, itemh, itemt in zip(list_user, list_hashtag, list_tweets):
      try:
        #The following is the same as the short version Recruited.create(**itemr)
        #a= Recruited.create(user_id = itemr['user_id'],screen_name = itemr['screen_name'],description=itemr['description'])
        a = Recruited.create(**itemr)
        b = Hashtag.create(**itemh)
        c = Tweets.create(**itemt)
        a.save()
        b.save()
        c.save()
      except IntegrityError:
        pass

    return list_user

t = Tw()
t.select_account()

db = SqliteDatabase('recruited.db')
db.connect()
new_recruit = Recruit(t, db)

list_recruited = new_recruit.search_and_save_users()

print( list(list_recruited) )