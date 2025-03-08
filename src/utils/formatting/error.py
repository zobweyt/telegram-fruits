__all__ = ["format_error_as_text"]

from aiogram.types import ErrorEvent
from aiogram.utils.formatting import Pre, Text, as_line


def format_error_as_text(event: ErrorEvent) -> Text:
    return as_line(
        "An unexpected exception occurred:",
        Pre(str(event.exception)),
        sep="\n\n",
    )
