class ProductCurrency:
    def __init__(self, product_id):
        self.product_id = product_id
        self.currencies = {}
        self.collection = db.product_currency_collection  # Aquí se establece la conexión con la base de datos

    def add_currency(self, currency_code, price):
        """Agrega una nueva moneda y su precio al producto"""
        self.currencies[currency_code] = price

    def update_currency(self, currency_code, new_price):
        """Actualiza el precio de una moneda específica para el producto"""
        if currency_code in self.currencies:
            self.currencies[currency_code] = new_price
        else:
            raise ValueError("La moneda no está disponible para este producto")

    def get_price(self, currency_code):
        """Devuelve el precio del producto en la moneda especificada"""
        if currency_code in self.currencies:
            return self.currencies[currency_code]
        else:
            raise ValueError("La moneda no está disponible para este producto")

    def save(self):
        """Guarda los cambios en la base de datos"""
        self.collection.update_one({"_id": self.product_id}, {"$set": {"currencies": self.currencies}}, upsert=True)

    def load(self):
        """Carga los datos de la base de datos para el producto"""
        data = self.collection.find_one({"_id": self.product_id})
        if data:
            self.currencies = data["currencies"]
        else:
            self.currencies = {}

