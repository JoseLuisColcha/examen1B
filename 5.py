import couchdb
import pymongo

couch_server=couchdb.Server()
couch_server.resource.credentials=('Jose Luis Colcha','1723547624')

couch_db = couch_server['freefire']

mongo_client= pymongo.MongoClient("localhost", 27017)
mongo_client_db = mongo_client.get_database('juego4')

for row in couch_db.view('_all_docs', include_docs=True):
    print(row['doc'])
    if mongo_client_db.freefire.count_documents({"_id":row['doc']['_id']})==0:
        mongo_client_db.freefire.insert(row['doc'])
