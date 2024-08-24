from orm.like import Like
from repository.base import Repository


class LikeRepository(Repository):
    model = Like

    def get_by_user_id_and_product_id(
        self,
        user_id: int,
        product_id: int
    ) -> Like:
        return self.session.query(
            self.model
        ).filter(
            self.model.user_id == user_id,
            self.model.product_id == product_id
        ).first()

    def get_by_product_id(
        self,
        product_id: int
    ) -> list[Like]:
        return self.session.query(
            self.model
        ).filter(
            self.model.product_id == product_id
        ).all()
