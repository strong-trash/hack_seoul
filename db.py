from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from settings import Settings


class Database:
    def __init__(self, settings: Settings):
        self.engine = create_engine(
            url=settings.get_db_url()
        )
        self.session = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    def get_session(self) -> Session:
        return self.session()

    def __new__(cls, settings: Settings):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance
