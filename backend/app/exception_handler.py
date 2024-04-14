import logging
from functools import wraps
from typing import Any, Callable

from fastapi import HTTPException, status
from pydantic import BaseModel

logging.getLogger().setLevel(logging.INFO)


def error_handler(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    async def decorator(*args: tuple[Any, ...], **kwargs: dict[str, Any]) -> BaseModel:
        try:
            return await func(*args, **kwargs)
        except HTTPException as e:
            logging.info("status code: %s, detail: %s", e.status_code, e.detail)
            raise HTTPException(status_code=e.status_code, detail=e.detail) from e
        except Exception as e:
            logging.info("status code: %s, detail: %s", status.HTTP_500_INTERNAL_SERVER_ERROR, e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}") from e
    return decorator
