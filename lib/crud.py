from pymongo import MongoClient
from bson.objectid import ObjectId

class MyMongoDB:
    
    def __init__(self, db_name, collection_name):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        
    def create(self, data):
        return self.collection.insert_one(data).inserted_id
    
    def read(self, id=None):
        if id:
            return self.collection.find_one({"_id": ObjectId(id)})
        else:
            return list(self.collection.find())
        
    def update(self, id, data):
        return self.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    
    def delete(self, id):
        return self.collection.delete_one({"_id": ObjectId(id)})
