from select import select
from aiogram.dispatcher.filters.state import StatesGroup, State


class GeneratePerson(StatesGroup):
    select_country = State()
    select_gender = State()