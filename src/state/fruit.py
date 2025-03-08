from aiogram.fsm.state import State, StatesGroup


class FruitStatesGroup(StatesGroup):
    SELECT = State()
    CREATE = State()
    DETAIL = State()
    EDIT = State()
