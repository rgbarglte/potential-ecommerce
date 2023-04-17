from pymongo import MongoClient

class ProductCollection:
    def __init__(self):
        # Conexión a la base de datos
        client = MongoClient()
        self.db = client['mi_basedatos']
        self.collection = self.db['productos']

    def create_product(self, product):
        """
        Crea un nuevo producto en la colección
        """
        self.collection.insert_one(product)

    def update_product(self, product_id, updates):
        """
        Actualiza un producto existente en la colección
        """
        self.collection.update_one({'_id': product_id}, {'$set': updates})

    def delete_product(self, product_id):
        """
        Elimina un producto de la colección
        """
        self.collection.delete_one({'_id': product_id})

    def get_product_by_id(self, product_id):
        """
        Obtiene un producto por su ID
        """
        return self.collection.find_one({'_id': product_id})

    def get_products_by_currency(self, currency):
        """
        Obtiene todos los productos que tengan una moneda específica
        """
        return self.collection.find({'currency': currency})

    def get_all_products(self):
        """
        Obtiene todos los productos de la colección
        """
        return self.collection.find()
