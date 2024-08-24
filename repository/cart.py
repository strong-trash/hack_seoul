from orm.cart import Cart
from repository.base import Repository


class CartRepository(Repository):
    model = Cart
