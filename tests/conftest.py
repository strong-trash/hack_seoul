import pytest
import pytest_asyncio
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

from app import create_app
from const import LikeStatus
from orm.base import Base
from orm.cart import Cart
from orm.like import Like
from orm.product import Product
from orm.user import User
from settings import TestSettings
from tests import helper


@pytest_asyncio.fixture(scope="session")
async def settings():
    return TestSettings()


@pytest_asyncio.fixture(scope="session")
async def test_fastapi_app(settings):
    return create_app(settings)


@pytest_asyncio.fixture(scope="function")
async def engine(settings):
    eng = create_engine(
        url=settings.get_db_url()
    )
    Base.metadata.create_all(eng)
    yield eng
    Base.metadata.drop_all(eng)


@pytest_asyncio.fixture(scope="function")
async def session(engine):
    sessionLocal = sessionmaker(engine)
    yield sessionLocal()


@pytest_asyncio.fixture(scope="function")
async def user():
    return [
        User(
            id=1,
            email=helper.TEST_USER_EMAIL_1,
            password=helper.TEST_USER_PASSWORD_1
        ),
        User(
            id=2,
            email=helper.TEST_USER_EMAIL_2,
            password=helper.TEST_USER_PASSWORD_2
        )
    ]


@pytest_asyncio.fixture(scope="function")
async def product():
    return [
        Product(
            id=1,
            name=helper.TEST_PRODUCT_NAME_1,
            image_path=helper.TEST_PRODUCT_IMAGE_PATH_1,
            price=helper.TEST_PRODUCT_PRICE_1,
            summary=helper.TEST_PRODUCT_SUMMARY_1
        ),
        Product(
            id=2,
            name=helper.TEST_PRODUCT_NAME_2,
            image_path=helper.TEST_PRODUCT_IMAGE_PATH_2,
            price=helper.TEST_PRODUCT_PRICE_2,
            summary=helper.TEST_PRODUCT_SUMMARY_2
        )
    ]


@pytest_asyncio.fixture(scope="function")
async def shopping_cart():
    return [
        Cart(
            id=1,
            user_id=1,
            product_id=1,
            count=5
        )
    ]


@pytest_asyncio.fixture(scope="function")
async def like():
    return [
        Like(
            id=1,
            is_like=LikeStatus.DISLIKE,
            user_id=1,
            product_id=1
        )
    ]


@pytest_asyncio.fixture(scope="function")
async def bootstrap(
    session,
    user,
    product,
    shopping_cart,
    like,
):
    session.bulk_save_objects(user)
    session.bulk_save_objects(product)
    session.bulk_save_objects(shopping_cart)
    session.bulk_save_objects(like)

    session.commit()

    yield "bootstrap"
