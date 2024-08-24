from typing import Annotated
from fastapi import Depends
from db import Database
from settings import Settings


async def get_settings() -> Settings:
    return Settings()


async def get_db(
    settings: Annotated[Settings, Depends(get_settings)]
) -> Database:
    return Database(settings)
