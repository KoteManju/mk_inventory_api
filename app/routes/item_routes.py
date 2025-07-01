from flask import Blueprint, request, jsonify
from app import db
from app.models.item import Item
from app.schemas.item_schema import ItemSchema
from app.utils.auth import jwt_required_custom
from flasgger import swag_from

item_bp = Blueprint('items', __name__)
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

@item_bp.route('/', methods=['GET'])
@jwt_required_custom
@swag_from({
    'responses': {
        200: {
            'description': 'List all items',
            'schema': {
                'type': 'array',
                'items': {
                    '$ref': '#/definitions/Item'
                }
            }
        }
    }
})
def get_items():
    items = Item.query.all()
    return items_schema.jsonify(items)

@item_bp.route('/', methods=['POST'])
@jwt_required_custom
def add_item():
    data = request.get_json()
    new_item = item_schema.load(data)
    db.session.add(new_item)
    db.session.commit()
    return item_schema.jsonify(new_item), 201
