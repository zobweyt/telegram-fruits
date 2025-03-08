__all__ = ["router"]

from aiogram import Router

from src.handlers.commands import start

router = Router()

router.include_routers(
    start.router,
)
