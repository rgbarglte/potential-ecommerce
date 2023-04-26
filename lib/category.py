from bson.objectid import ObjectId
from database.mongodb import *

class Category:
    def __init__(self): 
        self.collection = MONGODB['categories']
        
    def create(self, name):
        category = {'name': name}
        category_id = self.collection.insert_one(category).inserted_id
        return str(category_id)
        
    def read(self, category_id=None):
        if category_id:
            category = self.collection.find_one({'_id': ObjectId(category_id)})
            if category:
                category['_id'] = str(category['_id'])
                return category
            else:
                return None
        else:
            categories = []
            for category in self.collection.find():
                category['_id'] = str(category['_id'])
                categories.append(category)
            return categories
        
    def update(self, category_id, name):
        result = self.collection.update_one({'_id': ObjectId(category_id)}, {'$set': {'name': name}})
        if result.modified_count > 0:
            return True
        else:
            return False
        
    def delete(self, category_id):
        result = self.collection.delete_one({'_id': ObjectId(category_id)})
        if result.deleted_count > 0:
            return True
        else:
            return False
        
    def get_all_categorys(self):
        """
        Obtiene todos las categorias de la colección
        """
        return self.collection.find()

