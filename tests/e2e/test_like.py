import pytest
from fastapi import status
from httpx import ASGITransport, AsyncClient


@pytest.mark.asyncio
async def test_like_returns_201(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.post(
            "/like",
            headers={
                "Content-Type": "application/json"
            },
            json={
                "user_id": 2,
                "product_id": 1
            }
        )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
async def test_dislike_returns_201(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.post(
            "/dislike",
            headers={
                "Content-Type": "application/json"
            },
            json={
                "user_id": 2,
                "product_id": 1
            }
        )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
async def test_like_returns_201_when_update(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.post(
            "/like",
            headers={
                "Content-Type": "application/json"
            },
            json={
                "user_id": 1,
                "product_id": 1
            }
        )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
async def test_dislike_returns_201_when_update(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.post(
            "/dislike",
            headers={
                "Content-Type": "application/json"
            },
            json={
                "user_id": 2,
                "product_id": 2
            }
        )
    assert response.status_code == status.HTTP_201_CREATED
