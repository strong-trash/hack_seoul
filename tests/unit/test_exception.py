import pytest
from fastapi import status

from exception import BadRequestException, handle_exception


def test_exception_handler_returns_valid_response():
    response = handle_exception(None, BadRequestException())
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_exception_handler_not_implemented():
    with pytest.raises(NotImplementedError):
        handle_exception(None, RuntimeError())
