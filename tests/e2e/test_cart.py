import pytest
from fastapi import status
from httpx import ASGITransport, AsyncClient


@pytest.mark.asyncio
async def test_list_shoppingcart_returns_200(
    test_fastapi_app, bootstrap, shopping_cart
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.get("/cart/1")

    assert response.status_code == status.HTTP_200_OK

    result = response.json()
    assert len(result["products"]) == len(
        [i for i in shopping_cart if i.user_id == 1]
    )


@pytest.mark.asyncio
async def test_add_shoppingcart_returns_201(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.post(
            "/cart",
            headers={
                "Content-Type": "application/json"
            },
            json={
                "user_id": 1,
                "product_id": 2
            }
        )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
async def test_add_shoppingcart_returns_201_when_increment_count(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.post(
            "/cart",
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
async def test_update_shoppingcart_returns_202(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.put(
            "/cart/1",
            headers={
                "Content-Type": "application/json"
            },
            json={
                "count": 123
            }
        )

    assert response.status_code == status.HTTP_202_ACCEPTED


@pytest.mark.asyncio
async def test_update_shoppingcart_returns_400_when_invalid_count(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.put(
            "/cart/1",
            headers={
                "Content-Type": "application/json"
            },
            json={
                "count": 0
            }
        )

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_update_shoppingcart_returns_404(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.put(
            "/cart/-1",
            headers={
                "Content-Type": "application/json"
            },
            json={
                "count": 123
            }
        )

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
async def test_delete_shoppingcart_returns_204(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.delete(
            "/cart/1",
        )

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.asyncio
async def test_delete_shoppingcart_returns_404(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.delete(
            "/cart/-1",
        )

    assert response.status_code == status.HTTP_404_NOT_FOUND
