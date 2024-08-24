from dataclasses import dataclass

from command import Command


@dataclass(frozen=True)
class AddProductCommand(Command):
    name: str
    image_path: str
    price: int
    summary: str | None
