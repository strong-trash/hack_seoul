from orm.product import Product
from repository.base import Repository


class ProductRepository(Repository):
    model = Product

    def get_greater_than_id(self, id: int):
        return self.session.query(self.model).filter(self.model.id > id).first()
