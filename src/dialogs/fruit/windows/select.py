__all__ = ["fruit_select_window"]

from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.kbd import CurrentPage, NextPage, PrevPage, Row, ScrollingGroup, Select, SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from src.dialogs.fruit.keys import FRUIT_ID_KEY, FRUITS_KEY
from src.models.fruit import Fruit
from src.services.fruit import get_fruit_id, get_fruits
from src.state.fruit import FruitStatesGroup


async def _get_context(**kwargs: dict[str, Any]) -> dict[str, list[Fruit]]:
    fruits = get_fruits()

    return {
        FRUITS_KEY: fruits,
    }


async def _handle_click(
    callback_query: CallbackQuery,
    widget: Any,
    manager: DialogManager,
    selected_fruit_id: str,
) -> None:
    manager.dialog_data[FRUIT_ID_KEY] = selected_fruit_id

    await manager.switch_to(FruitStatesGroup.DETAIL)


fruit_select_window = Window(
    Const("Select a fruit:"),
    ScrollingGroup(
        Select(
            text=Format("{item.name}"),
            items=FRUITS_KEY,
            item_id_getter=get_fruit_id,
            on_click=_handle_click,
            id="fruit_select",
        ),
        width=1,
        height=3,
        hide_pager=True,
        id="fruit_scrolling_group",
    ),
    Row(
        PrevPage(
            text=Format("<"),
            scroll="fruit_scrolling_group",
        ),
        CurrentPage(
            text=Format("{current_page1}/{pages}"),
            scroll="fruit_scrolling_group",
        ),
        NextPage(
            text=Format(">"),
            scroll="fruit_scrolling_group",
        ),
    ),
    SwitchTo(
        text=Const("Add fruit"),
        state=FruitStatesGroup.CREATE,
        id="fruit_create",
    ),
    state=FruitStatesGroup.SELECT,
    getter=_get_context,
)
