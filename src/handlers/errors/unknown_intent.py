__all__ = ["handle_unknown_intent"]

from logging import getLogger

from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, ErrorEvent, Message, ReplyKeyboardRemove

logger = getLogger(__name__)


async def handle_unknown_intent(event: ErrorEvent) -> None:
    logger.warning("Restarting dialog:\n%s", event.exception)

    if event.update.callback_query:
        await _handle_unknown_intent_callback_query(event, event.update.callback_query)
    elif event.update.message:
        await _handle_unknown_intent_message(event, event.update.message)


async def _handle_unknown_intent_callback_query(event: ErrorEvent, callback_query: CallbackQuery) -> None:
    await callback_query.answer("The bot process has been restarted due to maintenance.")

    if not isinstance(callback_query.message, Message):
        return

    try:
        await callback_query.message.delete()
    except TelegramBadRequest:
        pass


async def _handle_unknown_intent_message(event: ErrorEvent, message: Message) -> None:
    await message.answer(
        "The bot process has been restarted due to maintenance.",
        reply_markup=ReplyKeyboardRemove(),
    )
