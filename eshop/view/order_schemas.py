from marshmallow import Schema, fields


class OrderCreateDtoSchema(Schema):
    product_ids = fields.List(fields.Str(), required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class OrderSchema(Schema):
    id = fields.String()
    product_ids = fields.List(fields.Str())
    total = fields.Float()


class OrderGetManyParams(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)
    page = fields.Int(missing=1)
    page_size = fields.Int(missing=10)


class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    price = fields.Float()