from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

@dataclass
class Response(Generic[T]):
    success: bool
    data: Optional[T] = None
    error: Optional[str] = None

    @staticmethod
    def ok(data: T):
        return Response(success=True, data=data)

    @staticmethod
    def fail(error: str):
        return Response(success=False, error=error)