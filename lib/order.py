from pymongo import MongoClient

class Order:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client['mydatabase']
        self.orders = self.db['orders']

    def create_order(self, user_id, products, total_amount, status='pending'):
        order = {
            'user_id': user_id,
            'products': products,
            'total_amount': total_amount,
            'status': status
        }
        return self.orders.insert_one(order)

    def get_order_by_id(self, order_id):
        return self.orders.find_one({'_id': ObjectId(order_id)})
    
    def get_orders_by_user_id(self, user_id):
        return self.orders.find({'user_id': user_id})

    def update_order_status(self, order_id, new_status):
        self.orders.update_one({'_id': ObjectId(order_id)}, {'$set': {'status': new_status}})

    def delete_order(self, order_id):
        self.orders.delete_one({'_id': ObjectId(order_id)})
