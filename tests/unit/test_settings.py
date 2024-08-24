from sqlalchemy import URL

from settings import Settings


def test_settings_get_db_url_returns_success():
    settings = Settings()
    url = settings.get_db_url()
    assert isinstance(url, URL)
