from flask import Blueprint, jsonify

orders_blueprint = Blueprint('orders', __name__,url_prefix='/orders')

@orders_blueprint.route('/')
def get_orders():
    # Código para obtener todas las órdenes
    orders = [{'id':213},{'id':213},{'id':213},{'id':213},{'id':213}]
    return jsonify(orders)

@orders_blueprint.route('/<int:order_id>')
def get_order(order_id):
    # Código para obtener una orden específica por ID
    order = {}
    return jsonify(order)

@orders_blueprint.route('/', methods=['POST'])
def create_order():
    # Código para crear una nueva orden
    return jsonify({'message': 'Orden creada exitosamente'})

@orders_blueprint.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    # Código para actualizar una orden específica por ID
    return jsonify({'message': 'Orden actualizada exitosamente'})

@orders_blueprint.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    # Código para eliminar una orden específica por ID
    return jsonify({'message': 'Orden eliminada exitosamente'})