import pickle
from tw import Tw

t = Tw()
t.select_account()
ids, screen_nameBot = t.getFollowers()

pickle.dump(ids, open("screen_names_" + screen_nameBot + ".p", "wb"))