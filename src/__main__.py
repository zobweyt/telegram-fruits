import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import ExceptionTypeFilter
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs
from aiogram_dialog.api.exceptions import UnknownIntent

from src import dialogs
from src.config import settings
from src.handlers import commands
from src.handlers.errors import handle_error, handle_unknown_intent


async def main() -> None:
    bot = Bot(
        token=settings.TELEGRAM_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    storage = MemoryStorage()

    dispatcher = Dispatcher(
        storage=storage,
    )

    dispatcher.errors.register(
        handle_error,
        F.update.message,
    )

    dispatcher.errors.register(
        handle_unknown_intent,
        ExceptionTypeFilter(UnknownIntent),
    )

    dispatcher.include_routers(
        dialogs.router,
        commands.router,
    )

    setup_dialogs(dispatcher)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
