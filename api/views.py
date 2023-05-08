from flask import Blueprint

# Importar los blueprints de los diferentes archivos
from api.products import products_blueprint
from api.customers import customers_blueprint
from api.orders import orders_blueprint
from api.coupon import coupon_blueprint

from flask import Blueprint, jsonify
 
# Crear el blueprint principal
api_blueprint = Blueprint('api', __name__ ,url_prefix='/api')

# Registrar los blueprints de los diferentes archivos
api_blueprint.register_blueprint(products_blueprint)
api_blueprint.register_blueprint(customers_blueprint)
api_blueprint.register_blueprint(orders_blueprint)
api_blueprint.register_blueprint(coupon_blueprint)
  