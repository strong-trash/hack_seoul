from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse


class BaseException(Exception):
    message = "Exception"


class BadRequestException(BaseException):
    message = "Bad Request"


class NotFoundException(BaseException):
    message = "Not Found"


exception_mapper = {
    BadRequestException: status.HTTP_400_BAD_REQUEST,
    NotFoundException: status.HTTP_404_NOT_FOUND,
}


def handle_exception(request: Request, exc: HTTPException):
    for exception in exception_mapper:
        if isinstance(exc, exception):
            return JSONResponse(
                status_code=exception_mapper[exception], content=exc.message
            )
    raise NotImplementedError
