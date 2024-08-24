

import pytest
from fastapi import status
from httpx import ASGITransport, AsyncClient


@pytest.mark.asyncio
async def test_ping(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.get("/ping")

    assert response.status_code == status.HTTP_200_OK
