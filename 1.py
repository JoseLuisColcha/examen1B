
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

###API ########################
ckey = "Khb64SZLHV1Ty3LnQ0R7fDWhy"
csecret = "HFVT0wetytjKon8NOrYiXcYCJxOmd8kEwMt0NctDh67v0dyY5g"
atoken = "1339955338657861633-XgBm27E9Qef183p67mR0om2pokkU3V"
asecret = "uRn0KBM34hySbYMNWAP3CTs1N9NwtKA97ME41t4tKuPeC"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://Jose Luis Colcha:1723547624@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('freefire')
except:
    db = server['freefire']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[-9.47,36.55,-0.54,42.4])  
twitterStream.filter(track=['freefire'])
