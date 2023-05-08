from flask import Blueprint, jsonify , request
from lib.coupon import Coupon

coupon_blueprint = Blueprint('coupon', __name__,url_prefix='/coupon')

@coupon_blueprint.route('/')
def get_coupons(): 
    return jsonify(Coupon().get_coupons())

@coupon_blueprint.route('/<int:coupon_id>')
def get_coupon(coupon_id): 
    return jsonify(Coupon().get_by_id(coupon_id))

@coupon_blueprint.route('/', methods=['POST'])
def create_order(): 
    data = request.get_json()
    create = Coupon().create(
        name=data.get('name','Cupon borrador'),
        code=data.get('code',None),
        description=data.get('description','Cupon borrador'),
        discount=data.get('discount',50),
        date=data.get('date','2023-07-23') 
    ) 
    return jsonify(create)

@coupon_blueprint.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id): 
    return jsonify({'message': 'Orden actualizada exitosamente'})

@coupon_blueprint.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id): 
    return jsonify(Coupon().delete(order_id))