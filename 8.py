import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb

try:
    client = MongoClient('localhost')
    print (client.list_database_names())
    clientatl = MongoClient("mongodb+srv://esfot:esfot@cluster0.cyxcn.mongodb.net/twitter?retryWrites=true&w=majority")
    print (clientatl.list_database_names())
except requests.ConnectionError as e:
    raise e


db = client['juego2']
col = db['freefire']
dbatl = clientatl['mongo2mongoatlas']
colatl = dbatl['freefire']

for doc in col.find({}):
    print(doc)
    
for doc in col.find({}):
    colatl.insert_one(doc)
    print(doc)

for doc in colatl.find({}):
    print(doc)