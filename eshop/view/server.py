from flask import Flask, request
from marshmallow import ValidationError

from eshop.businsess_logic.order_usecases import order_create, order_get_many, order_get_by_id
from eshop.view.order_schemas import OrderCreateDtoSchema, OrderSchema, OrderGetManyParams

from eshop.businsess_logic.product_usecases import (
    product_create, product_get_many, product_get_by_id
)
from eshop.view.order_schemas import (
    ProductCreateDtoSchema, ProductSchema, ProductGetManyParams
)

app = Flask(__name__)


@app.post("/api/v1/order")
def order_create_endpoint():
    try:
        order_create_dto = OrderCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        order = order_create(
            product_ids=order_create_dto['product_ids']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return OrderSchema().dump(order)


@app.get("/api/v1/order")
def order_get_many_endpoint():
    try:
        order_get_many_params = OrderGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    order = order_get_many(
        page=order_get_many_params['page'],
        limit=order_get_many_params['limit'],
    )

    return OrderSchema(many=True).dump(order)


@app.get("/api/v1/order/<id>")
def order_get_by_id_endpoint(id):
    order = order_get_by_id(id)

    if order is None:
        return {
            "error": 'Not found'
        }, 404

    return OrderSchema().dump(order)

@app.post("/api/v1/product")
def product_create_endpoint():
    try:
        dto = ProductCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400
    product = product_create(name=dto["name"], price=dto["price"])
    return ProductSchema().dump(product)

@app.get("/api/v1/product")
def product_get_many_endpoint():
    try:
        params = ProductGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400
    products = product_get_many(page=params["page"], page_size=params["page_size"])
    return ProductSchema(many=True).dump(products)

@app.get("/api/v1/product/<int:product_id>")
def product_get_by_id_endpoint(product_id):
    try:
        product = product_get_by_id(product_id)
    except Exception as e:
        return {"error": str(e)}, 404
    return ProductSchema().dump(product)


def run_server():
    app.run()

