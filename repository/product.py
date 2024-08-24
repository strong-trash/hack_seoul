from orm.product import Product
from repository.base import Repository


class ProductRepository(Repository):
    model = Product
