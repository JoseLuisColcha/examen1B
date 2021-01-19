from facebook_scraper import get_posts
import pymongo
import json
import time

myclient = pymongo.MongoClient("mongodb://localhost:27017") 

try:
    mydb=myclient['juego2']
    mycol=mydb['freefire']
except:
    mydb=myclient['juego2']
    mycol=mydb['freefire']
    
i=1
for post in get_posts('FreeFireSA/?brand_redir=1799852050043976', pages=1000, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}


        doc['post_url']=post['post_url']
        mycol.insert_one(doc)

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))    