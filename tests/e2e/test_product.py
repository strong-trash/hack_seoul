import pytest
from fastapi import status
from httpx import ASGITransport, AsyncClient

from tests import helper


@pytest.mark.asyncio
async def test_show_product_detail_returns_200(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.get("/product/0/1")

    assert response.status_code == status.HTTP_200_OK

    result = response.json()

    assert result["name"] == helper.TEST_PRODUCT_NAME_1
    assert result["price"] == helper.TEST_PRODUCT_PRICE_1
    assert result["summary"] == helper.TEST_PRODUCT_SUMMARY_1
    assert result["image_path"] == helper.TEST_PRODUCT_IMAGE_PATH_1


@pytest.mark.asyncio
async def test_show_product_detail_returns_200_when_last_id(
    test_fastapi_app, bootstrap
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.get("/product/100/1")

    assert response.status_code == status.HTTP_200_OK

    result = response.json()

    assert result["name"] == helper.TEST_PRODUCT_NAME_1
    assert result["price"] == helper.TEST_PRODUCT_PRICE_1
    assert result["summary"] == helper.TEST_PRODUCT_SUMMARY_1
    assert result["image_path"] == helper.TEST_PRODUCT_IMAGE_PATH_1


@pytest.mark.asyncio
async def test_list_product_returns_200(
    test_fastapi_app, bootstrap, product
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.get("/product")

    assert response.status_code == status.HTTP_200_OK

    result = response.json()

    assert len(result["products"]) == len(product)


@pytest.mark.asyncio
async def test_add_product_returns_201(
    test_fastapi_app, bootstrap, product
):
    async with AsyncClient(
        transport=ASGITransport(app=test_fastapi_app), base_url="http://test"
    ) as client:
        response = await client.post(
            "/product",
            headers={
                "Content-Type": "application/json"
            },
            json={
                "name": "product_name",
                "image_path": "product_image_path",
                "price": 50000,
            }
        )

    assert response.status_code == status.HTTP_201_CREATED
