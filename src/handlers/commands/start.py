__all__ = ["router"]

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode, StartMode

from src.state.fruit import FruitStatesGroup

router = Router(name=__name__)


@router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(
        FruitStatesGroup.SELECT,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.SEND,
    )
