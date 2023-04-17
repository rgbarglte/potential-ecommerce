from typing import List
from datetime import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient


class Cart:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.items = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.db = MongoClient()['myapp']['carts']

    def add_item(self, product_id: str, quantity: int):
        for item in self.items:
            if item['product_id'] == product_id:
                item['quantity'] += quantity
                break
        else:
            self.items.append({'product_id': product_id, 'quantity': quantity})
        self.updated_at = datetime.now()
        self.save()

    def remove_item(self, product_id: str):
        self.items = [item for item in self.items if item['product_id'] != product_id]
        self.updated_at = datetime.now()
        self.save()

    def update_item_quantity(self, product_id: str, quantity: int):
        for item in self.items:
            if item['product_id'] == product_id:
                item['quantity'] = quantity
                break
        self.updated_at = datetime.now()
        self.save()

    def get_items(self) -> List:
        return self.items

    def save(self):
        cart = {
            '_id': ObjectId(),
            'user_id': self.user_id,
            'items': self.items,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        self.db.insert_one(cart)

    @staticmethod
    def get_cart(cart_id: str) -> dict:
        return MongoClient()['myapp']['carts'].find_one({'_id': ObjectId(cart_id)})

