from flask import Blueprint, jsonify

customers_blueprint = Blueprint('customers', __name__, url_prefix='/customers')

@customers_blueprint.route('/', methods=['GET'])
def get_all_customers():
    # Obtiene todos los clientes
    customers = [{"id": 1, "name": "John Doe", "email": "johndoe@gmail.com"},
                 {"id": 2, "name": "Jane Doe", "email": "janedoe@gmail.com"}]

    return jsonify(customers)

@customers_blueprint.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    # Obtiene un cliente por su ID
    customer = {"id": customer_id, "name": "John Doe", "email": "johndoe@gmail.com"}

    return jsonify(customer)

@customers_blueprint.route('/', methods=['POST'])
def create_customer():
    # Crea un nuevo cliente
    customer = {"id": 3, "name": "Alice Smith", "email": "alicesmith@gmail.com"}

    return jsonify(customer)

@customers_blueprint.route('/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    # Actualiza un cliente existente por su ID
    customer = {"id": customer_id, "name": "Alice Smith", "email": "alicesmith@gmail.com"}

    return jsonify(customer)

@customers_blueprint.route('/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    # Elimina un cliente existente por su ID
    return '', 204
