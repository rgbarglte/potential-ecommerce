from flask import Blueprint
 
products_blueprint = Blueprint('products', __name__, url_prefix='/products')


@products_blueprint.route('/', methods=['GET'])
def get_products():
    # Lógica para obtener todos los productos
    return 'Todos los productos'


@products_blueprint.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # Lógica para obtener un producto en específico
    return f'Producto con id {product_id}'


@products_blueprint.route('/', methods=['POST'])
def create_product():
    # Lógica para crear un nuevo producto
    return 'Crear un nuevo producto'


@products_blueprint.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # Lógica para actualizar un producto en específico
    return f'Actualizar el producto con id {product_id}'


@products_blueprint.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Lógica para eliminar un producto en específico
    return f'Eliminar el producto con id {product_id}'
