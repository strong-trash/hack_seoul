from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm.session import Session

from const import LikeStatus
from depends import get_session
from dto.cart import CartDto, CartResponseDto, CartResponseModel, CartUpdateDto
from dto.like import LikeDto
from dto.product import ProductDto
from exception import BadRequestException, BaseException, NotFoundException, handle_exception
from orm.cart import Cart
from orm.like import Like
from orm.product import Product
from repository.cart import CartRepository
from repository.like import LikeRepository
from repository.product import ProductRepository

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(BaseException, handle_exception)


@app.get("/ping", status_code=status.HTTP_200_OK)
async def ping() -> str:
    return "pong"


@app.post("/like", status_code=status.HTTP_201_CREATED)
async def like(
    like_data: LikeDto,
    session: Annotated[Session, Depends(get_session)]
) -> LikeDto:
    repository = LikeRepository(session)
    obj = repository.get_by_user_id_and_product_id(
        user_id=like_data.user_id,
        product_id=like_data.product_id
    )
    if obj is None:
        obj = Like(
            user_id=like_data.user_id,
            product_id=like_data.product_id,
            is_like=LikeStatus.LIKE
        )
        repository.add(obj)
    elif obj.is_like == LikeStatus.DISLIKE:
        obj.is_like = LikeStatus.LIKE

    return like_data


@app.post("/dislike", status_code=status.HTTP_201_CREATED)
async def dislike(
    like_data: LikeDto,
    session: Annotated[Session, Depends(get_session)]
) -> LikeDto:
    repository = LikeRepository(session)
    obj = repository.get_by_user_id_and_product_id(
        user_id=like_data.user_id,
        product_id=like_data.product_id
    )
    if obj is None:
        obj = Like(
            user_id=like_data.user_id,
            product_id=like_data.product_id,
            is_like=LikeStatus.DISLIKE
        )
        repository.add(obj)
    elif obj.is_like == LikeStatus.LIKE:
        obj.is_like = LikeStatus.DISLIKE

    return like_data


@app.get("/product/{product_id}", status_code=status.HTTP_200_OK)
async def show_product(
    product_id: int,
    session: Annotated[Session, Depends(get_session)]
):
    repository = ProductRepository(session)
    product = repository.get_greater_than_id(product_id)
    if product is None:
        product = repository.get_greater_than_id(0)
    return product


@app.post("/product", status_code=status.HTTP_201_CREATED)
async def add_product(
    product: ProductDto,
    session: Annotated[Session, Depends(get_session)]
) -> ProductDto:
    repository = ProductRepository(session)
    obj = Product(
        name=product.name,
        image_path=product.image_path,
        price=product.price,
        summary=product.summary
    )
    repository.add(obj)
    return product


@app.get("/cart/{user_id}", status_code=status.HTTP_200_OK)
async def list_shoppingcart(
    user_id: int,
    session: Annotated[Session, Depends(get_session)]
) -> CartResponseModel:
    repository = CartRepository(session)

    cart_products = repository.get_by_user_id(user_id)
    products = [
        CartResponseDto.from_entity(cart_product)
        for cart_product in cart_products
    ]
    return CartResponseModel(
        products=products
    )


@app.post("/cart", status_code=status.HTTP_201_CREATED)
async def add_shoppingcart(
    cart: CartDto,
    session: Annotated[Session, Depends(get_session)]
) -> CartDto:
    repository = CartRepository(session)
    obj = Cart(
        user_id=cart.user_id,
        product_id=cart.product_id,
        count=1
    )
    repository.add(obj)
    return cart


@app.put("/cart/{cart_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_shoppingcart(
    cart_id: int,
    cart: CartUpdateDto,
    session: Annotated[Session, Depends(get_session)]
) -> CartUpdateDto:
    if cart.count <= 0:
        raise BadRequestException
    repository = CartRepository(session)
    obj = repository.get_by_id(cart_id)
    if obj is None:
        raise NotFoundException
    obj.count = cart.count

    return cart


@app.delete("/cart/{cart_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shoppingcart(
    cart_id: int,
    session: Annotated[Session, Depends(get_session)]
) -> None:
    repository = CartRepository(session)
    obj = repository.get_by_id(cart_id)
    if obj is None:
        raise NotFoundException
    repository.delete(obj)
