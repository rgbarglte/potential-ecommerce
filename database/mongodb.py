from pymongo import MongoClient 
MONGODB_HOST = "mongodb+srv://admin:43119739Ramiro@cluster0.kewdh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_HOST)
MONGODB = client['test']

 