from database.mongodb import MONGODB
from bson.objectid import ObjectId


class Address:
    def __init__(self, address_id=None):
        self.collection = MONGODB['address']
        if address_id:
            self.address = self.collection.find_one({'_id': ObjectId(address_id)})
        else:
            self.address = {}

    def create(self, user_id, name, address, city, state, zip_code, country):
        self.address = {
            'user_id': ObjectId(user_id),
            'name': name,
            'address': address,
            'city': city,
            'state': state,
            'zip_code': zip_code,
            'country': country
        }
        self.collection.insert_one(self.address)

    def update(self, name=None, address=None, city=None, state=None, zip_code=None, country=None):
        update_data = {}
        if name:
            update_data['name'] = name
        if address:
            update_data['address'] = address
        if city:
            update_data['city'] = city
        if state:
            update_data['state'] = state
        if zip_code:
            update_data['zip_code'] = zip_code
        if country:
            update_data['country'] = country

        self.collection.update_one({'_id': self.address['_id']}, {'$set': update_data})
        self.address = self.collection.find_one({'_id': self.address['_id']})

    def delete(self):
        self.collection.delete_one({'_id': self.address['_id']})

    @classmethod
    def find_by_user_id(cls, user_id): 
        collection = MONGODB['address']
        addresses = []
        for address in collection.find({'user_id': ObjectId(user_id)}):
            addresses.append(Address(str(address['_id'])))
        return addresses

