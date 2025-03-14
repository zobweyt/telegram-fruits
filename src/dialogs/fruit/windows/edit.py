__all__ = ["fruit_edit_window"]

from typing import Any, cast

from aiogram.types import Message
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const

from src.dialogs.fruit.keys import FRUIT_ID_KEY
from src.models.fruit import validate_fruit_name
from src.services.fruit import update_fruit
from src.state.fruit import FruitStatesGroup


async def _handle_error(message: Message, dialog: Any, manager: DialogManager, error: ValueError) -> None:
    await message.answer(error.args[0])


async def _handle_success(message: Message, dialog: Any, dialog_manager: DialogManager, new_name: str) -> None:
    selected_fruit_raw_id = dialog_manager.dialog_data.get(FRUIT_ID_KEY)
    selected_fruit_id = cast(str, selected_fruit_raw_id)

    update_fruit(selected_fruit_id, new_name)

    await dialog_manager.switch_to(FruitStatesGroup.DETAIL)


fruit_edit_window = Window(
    Const("Enter the new name of the fruit:"),
    TextInput(
        on_error=_handle_error,
        on_success=_handle_success,
        type_factory=validate_fruit_name,
        id="fruit_name",
    ),
    SwitchTo(
        text=Const("❌ Cancel"),
        state=FruitStatesGroup.DETAIL,
        id="fruit_edit_cancel",
    ),
    state=FruitStatesGroup.EDIT,
)
