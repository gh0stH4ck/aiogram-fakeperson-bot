from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender

from loader import dp

from keyboards.default.country import country_kb
from keyboards.default.gender import gender_select

from states.person_gen import GeneratePerson


@dp.message_handler(Command("person"))
async def new_person(message: types.Message, state: FSMContext):
    await message.answer("Выберите страну проживания вашей личности.", reply_markup=country_kb)
    
    await GeneratePerson.select_country.set()


@dp.message_handler(text="Россия", state=GeneratePerson.select_country)
async def select_gender(message: types.Message, state: FSMContext):
    country = message.text
    await message.answer("Выберите пол вашей личности", reply_markup=gender_select)
    
    async with state.proxy() as data:
        data["country"] = country

    await GeneratePerson.select_gender.set()


@dp.message_handler(text="Украина")
async def ukraine(message: types.Message):
    await message.answer("ukr")


@dp.message_handler(text="США")
async def usa(message: types.Message):
    await message.answer("usa")


@dp.message_handler(state=GeneratePerson.select_gender)
async def get_person(message: types.Message, state: FSMContext):
    country = await state.get_data("country")
    gender = message.text

    await message.answer(f"country: {country.get('country')} gender: {gender}")