from typing import Optional, List

from eshop.businsess_logic.product import Product
from eshop.data_access.product_repo import ProductRepo



def product_create(dto) -> Product:
    raise Exception('Not implemented yet')


def product_get_by_id(id: str) -> Optional[Product]:
    raise Exception('Not implemented yet')


def product_get_many(page: int, limit: int) -> List[Product]:
    raise Exception('Not implemented yet')

def product_create(name: str, price: float) -> Product:
    product = Product(name=name, price=price)
    return ProductRepo().save(product)

def product_get_many(page: int, page_size: int) -> list[Product]:
    return ProductRepo().get_many(page, page_size)

def product_get_by_id(product_id: int) -> Product:
    return ProductRepo().get_by_id(product_id)