__all__ = [
    "create_fruit",
    "delete_fruit",
    "get_fruit_id",
    "get_fruit",
    "get_fruits",
    "update_fruit",
]

from uuid import uuid4

from src.models.fruit import Fruit

_fruits: list[Fruit] = [
    Fruit(id=str(uuid4()), name="🍏 Apple"),
    Fruit(id=str(uuid4()), name="🍌 Banana"),
    Fruit(id=str(uuid4()), name="🍊 Orange"),
    Fruit(id=str(uuid4()), name="🍐 Pear"),
]


def create_fruit(new_name: str) -> Fruit:
    global _fruits

    new_id = str(uuid4())
    new_fruit = Fruit(id=new_id, name=new_name)

    _fruits.append(new_fruit)

    return new_fruit


def delete_fruit(fruit_id: str) -> None:
    global _fruits

    _fruits = [fruit for fruit in _fruits if fruit.id != fruit_id]


def get_fruit_id(fruit: Fruit) -> str:
    return fruit.id


def get_fruit(fruit_id: str) -> Fruit | None:
    global _fruits

    fruit = next((fruit for fruit in _fruits if fruit.id == fruit_id), None)

    return fruit


def get_fruits() -> list[Fruit]:
    global _fruits

    return _fruits


def update_fruit(fruit_id: str, new_name: str) -> None:
    global _fruits

    fruit = get_fruit(fruit_id)

    if fruit is None:
        return

    fruit.name = new_name
