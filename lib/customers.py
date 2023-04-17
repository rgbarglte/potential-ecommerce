from pymongo import MongoClient
from bson.objectid import ObjectId

class User:
    def __init__(self, username=None, email=None, password=None):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['myapp']
        self.collection = self.db['users']
        self.username = username
        self.email = email
        self.password = password

    def create(self):
        new_user = {
            'username': self.username,
            'email': self.email,
            'password': self.password
        }
        self.collection.insert_one(new_user)

    def read(self, user_id=None):
        if user_id:
            user = self.collection.find_one({'_id': ObjectId(user_id)})
        else:
            user = self.collection.find_one({'email': self.email})
        return user

    def update(self, user_id, update_dict):
        self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': update_dict})

    def delete(self, user_id):
        self.collection.delete_one({'_id': ObjectId(user_id)})
