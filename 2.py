import requests
import pandas as pd
from bs4 import BeautifulSoup
import pymongo
import json

def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))   

response = requests.get("https://ecuador.patiotuerca.com/usados/-/autos?type_autos_moderated=moderated")
soup = BeautifulSoup(response.content, "lxml")

Tittle=[]
Price=[]
Description=[]

post_tittle=soup.find_all("h4", class_="bold size-h6 left")
post_price=soup.find_all("span", class_="left share-value")
post_description=soup.find_all("span", class_="latam-secondary-text text-lighten-2 negotiable-txt left")


for element in post_tittle:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Tittle.append(limpio.strip())

for element in post_price:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Price.append(limpio.strip())

for element in post_description:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Description.append(limpio.strip())

dfDS=pd.DataFrame({'tittle':Tittle,'price':Price,'description':Description})


#=====================mongoDB=============================
myclient = pymongo.MongoClient("mongodb://localhost:27017")  
try:
    mydb=myclient['datospagina']
    mycol=mydb['autos']
except:
    mydb=myclient['datospagina']
    mycol=mydb['autos']

doc={}
for i in range(len(dfDS)): 
    i= i+1
    try:
        doc['_id']=i

        doc['title']=dfDS.iloc[i,0]
        doc['price']=dfDS.iloc[i,1]
        doc['descripcion']=dfDS.iloc[i,2]

        mycol.insert_one(doc)
        print(doc)
        print("guardado exitosamente")

    except Exception as e:    
            print("no se pudo grabar:" + str(e))