__all__ = ["fruit_detail_window"]

from typing import Any, cast

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, Row, SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from src.dialogs.fruit.keys import FRUIT_ID_KEY, FRUIT_KEY
from src.models.fruit import Fruit
from src.services.fruit import delete_fruit, get_fruit
from src.state.fruit import FruitStatesGroup


async def _get_context(dialog_manager: DialogManager, **kwargs: dict[str, Any]) -> dict[str, Fruit | None]:
    selected_fruit_raw_id = dialog_manager.dialog_data.get(FRUIT_ID_KEY)
    selected_fruit_id = cast(str, selected_fruit_raw_id)
    selected_fruit = get_fruit(selected_fruit_id)

    return {
        FRUIT_KEY: selected_fruit,
    }


async def _delete_fruit(callback_query: CallbackQuery, widget: Any, dialog_manager: DialogManager) -> None:
    selected_fruit_raw_id = dialog_manager.dialog_data.get(FRUIT_ID_KEY)
    selected_fruit_id = cast(str, selected_fruit_raw_id)

    delete_fruit(selected_fruit_id)

    await callback_query.answer("Fruit deleted successfully!")
    await dialog_manager.switch_to(FruitStatesGroup.SELECT)


fruit_detail_window = Window(
    Format("{fruit.name}\n"),
    Format("ID: {fruit.id}"),
    Row(
        SwitchTo(
            text=Const("✏️ Edit"),
            state=FruitStatesGroup.EDIT,
            id="fruit_edit",
        ),
        Button(
            text=Const("🗑️ Delete"),
            on_click=_delete_fruit,
            id="fruit_delete",
        ),
    ),
    SwitchTo(
        text=Const("⬅️ Back"),
        id="fruit_edit_back",
        state=FruitStatesGroup.SELECT,
    ),
    state=FruitStatesGroup.DETAIL,
    getter=_get_context,
)
