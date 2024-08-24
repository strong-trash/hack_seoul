from command.cart import AddCartCommand, DeleteCartCommand, UpdateCartCommand
from dto.cart import CartDto, CartUpdateDto


async def add_cart_command(cart: CartDto):
    return AddCartCommand(
        user_id=cart.user_id,
        product_id=cart.product_id
    )


async def update_cart_command(cart: CartUpdateDto, cart_id: int):
    return UpdateCartCommand(
        cart_id=cart_id,
        count=cart.count
    )


async def delete_cart_command(cart_id: int):
    return DeleteCartCommand(
        cart_id=cart_id
    )
