import pymongo
import json
from logging_class import lg

#load JSON and push to mongodb

try:
    client = pymongo.MongoClient("mongodb+srv://achowdh:failsafe@agnik0.mmtem.mongodb.net/?retryWrites=true&w=majority")
    db = client.test

    with open(r"C:\Users\agnik\attribute.json") as file:
        data = [(json.load(file))]

    db = client['dress']
    collection = db["dress_attribute"]

    collection.insert_many(data)
    lg.info("data push success")
except Exception as e:

    lg.error(e)