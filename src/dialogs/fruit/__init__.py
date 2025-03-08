__all__ = ["fruit_dialog"]

from aiogram_dialog import Dialog

from src.dialogs.fruit.windows.create import fruit_create_window
from src.dialogs.fruit.windows.detail import fruit_detail_window
from src.dialogs.fruit.windows.edit import fruit_edit_window
from src.dialogs.fruit.windows.select import fruit_select_window

fruit_dialog = Dialog(
    fruit_select_window,
    fruit_create_window,
    fruit_detail_window,
    fruit_edit_window,
)
