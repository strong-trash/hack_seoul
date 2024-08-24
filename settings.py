from typing import override

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )

    db_name: str = str()
    db_user: str = str()
    db_password: str = str()
    db_host: str = str()
    db_port: int = int()

    def get_db_url(self):
        return URL.create(
            drivername="mysql+pymysql",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
        )


class TestSettings(Settings):
    @override
    def get_db_url(self):
        return "sqlite:///pangtok.db"
