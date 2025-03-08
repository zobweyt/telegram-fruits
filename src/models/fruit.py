__all__ = [
    "FRUIT_NAME_MAX_LENGTH",
    "Fruit",
    "validate_fruit_name",
]

from pydantic import BaseModel

FRUIT_NAME_MAX_LENGTH = 16


class Fruit(BaseModel):
    id: str
    name: str


def validate_fruit_name(new_name: str) -> str:
    if len(new_name) > FRUIT_NAME_MAX_LENGTH:
        raise ValueError(f"Fruit name must be at most {FRUIT_NAME_MAX_LENGTH} characters long.")
    return new_name
