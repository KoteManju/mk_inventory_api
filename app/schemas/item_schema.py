from app import ma
from app.models.item import Item

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        load_instance = True

from app import ma
from app.models.item import Item
from marshmallow import fields

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        load_instance = True

    name = fields.String(required=True)
    quantity = fields.Integer(required=True)
    price = fields.Float(required=True)
    description = fields.String(required=False)  # ✅ allow optional description
