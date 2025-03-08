__all__ = ["router"]

from aiogram import Router

from src.dialogs.fruit import fruit_dialog

router = Router()

router.include_routers(
    fruit_dialog,
)
