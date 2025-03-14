__all__ = ["fruit_create_window"]

from typing import Any

from aiogram.types import Message
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const

from src.dialogs.fruit.keys import FRUIT_ID_KEY
from src.models.fruit import validate_fruit_name
from src.services.fruit import create_fruit
from src.state.fruit import FruitStatesGroup


async def _handle_error(message: Message, dialog: Any, manager: DialogManager, error: ValueError) -> None:
    await message.answer(error.args[0])


async def _handle_success(message: Message, dialog: Any, manager: DialogManager, new_name: str) -> None:
    new_fruit = create_fruit(new_name)

    manager.dialog_data[FRUIT_ID_KEY] = new_fruit.id

    await manager.switch_to(FruitStatesGroup.DETAIL)


fruit_create_window = Window(
    Const("Enter name of the new fruit:"),
    TextInput(
        on_error=_handle_error,
        on_success=_handle_success,
        type_factory=validate_fruit_name,
        id="fruit_name",
    ),
    SwitchTo(
        text=Const("❌ Cancel"),
        state=FruitStatesGroup.SELECT,
        id="fruit_create_cancel",
    ),
    state=FruitStatesGroup.CREATE,
)
