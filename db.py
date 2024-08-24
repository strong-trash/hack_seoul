from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from settings import Settings


class Database:
    def __init__(self, settings: Settings):
        url = URL.create(
            drivername="mysql+pymysql",
            username=settings.db_user,
            password=settings.db_password,
            host=settings.db_host,
            port=settings.db_port,
            database=settings.db_name
        )
        self.engine = create_engine(
            url=url, echo=True
        )
        self.session = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    def get_session(self) -> Session:
        return self.session()

    # TODO: singleton implementation
    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(Database, cls).__new__(cls)
    #     return cls.instance
