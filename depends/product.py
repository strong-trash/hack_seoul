from command.product import AddProductCommand
from dto.product import ProductDto


async def add_product_command(product: ProductDto):
    return AddProductCommand(
        name=product.name,
        image_path=product.image_path,
        price=product.price,
        summary=product.summary
    )
