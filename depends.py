from typing import Annotated

from fastapi import Depends

from db import Database
from settings import Settings


async def get_settings() -> Settings:
    return Settings()


async def get_database(
    settings: Annotated[Settings, Depends(get_settings)]
) -> Database:
    return Database(settings)


async def get_session(
    database: Annotated[Database, Depends(get_database)]
):
    session = database.get_session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
