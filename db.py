import pymysql
from settings import Settings


class Database:
    def __init__(self, settings: Settings):
        self.connection = pymysql.connect(
            host=settings.db_host,
            user=settings.db_user,
            password=settings.db_password,
            db=settings.db_name,
            port=settings.db_port,
            charset='utf8'
        )

        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)

    # TODO: singleton implementation
    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(Database, cls).__new__(cls)
    #     return cls.instance
