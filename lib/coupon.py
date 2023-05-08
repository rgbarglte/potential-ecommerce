from database.mongodb import MONGODB
from bson.objectid import ObjectId
from datetime import datetime
import random
import string

# Formato de fecha esperado : YYYY-MM-DD

class Coupon:
    def __init__(self, coupon_id=None):
        self.collection = MONGODB['coupon']
        if coupon_id:
            self.coupon = self.collection.find_one({'_id': ObjectId(coupon_id)})
        else:
            self.coupon = {}

    def get_coupons(self):
        find = self.collection.find({})
        find = list(find)
        results = []
        if not find:
            return []
        for e in find:
            e['_id'] = str(e['_id'])
            results.append(e)
        return results
    
    def generate_discount_code(self,length):
        characters = string.ascii_letters + string.digits  # Letras mayúsculas, minúsculas y dígitos
        code = ''.join(random.choice(characters) for _ in range(length))
        return code

    def get_by_code(self,code:str):
        find = self.collection.find_one({'name': code})
        if find:
            return find
        return False
    
    def get_by_id(self,id:str):
        find = self.collection.find_one({'name': ObjectId(id)})
        if find:
            return find
        return False

    
    def create(self,name:str,code:str,description:str,discount:int,date:str):
        if code is None:
            code = self.generate_discount_code(5)
            if self.get_by_code(code):
                code = self.generate_discount_code(6)

        # self.coupon = {
        #     'name' : name,
        #     'code': code,
        #     'description' : description,
        #     'discount': discount,
        #     'expiration_date': datetime.strptime(date, '%Y-%m-%d')
        # }
        coupon = {
            'name' : name,
            'code': code,
            'description' : description,
            'discount': discount,
            'expiration_date': datetime.strptime(date, '%Y-%m-%d')
        }
        insert = self.collection.insert_one(self.coupon)
        if not insert:
            return False
        return {'result':coupon , '_id' : str(insert.inserted_id) } 

    def update(self,id:str,data : object):
        existing_document = self.get_by_id(id)

        # Actualizar los valores del documento con los valores de data si no existen
        for key, value in data.items():
            existing_document[key] = existing_document.get(key, value)

        update = self.collection.update_one({'_id': ObjectId(id)}, {'$set': existing_document})
        if not update:
            return False
        return update

    def delete(self,id:str):
        self.collection.delete_one({'_id': ObjectId(id)})
        return True
 
