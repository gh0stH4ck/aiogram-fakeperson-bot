import random as r

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hbold, hitalic

from mimesis import Person, Address
from mimesis.locales import Locale
from mimesis.enums import Gender

from loader import dp


from keyboards.default.country import country_kb
from keyboards.default.gender import gender_select

from states.person_gen import GeneratePerson


def send(name, birthday, email, phone, height, weight, eye, polit) -> str:
    return f"""
👤 Имя и фамилия: {hbold(name)}
🎂 День рождения(Д,М,Г): {hbold(birthday)}
📪 Почта: {hbold(email)}
☎️ Телефон: {hbold(phone)}

📢 Рост: {hbold(height)} см.
⚖️ Вес: {hbold(weight)} кг.
👁️ Цвет глаз: {hbold(eye)}
🚨 Политические взгляды: {hbold(polit)}

{hitalic('/person')} - Создать новую личность. 
"""

@dp.message_handler(Command("person"))
async def new_person(message: types.Message, state: FSMContext):
    await message.answer("🗾 Выберите страну проживания вашей личности.", reply_markup=country_kb)

    await GeneratePerson.select_country.set()

@dp.message_handler(text="Россия", state=GeneratePerson.select_country)
async def select_gender(message: types.Message, state: FSMContext):
    country = message.text
    await message.answer("👤 Выберите пол вашей личности", reply_markup=gender_select)
    
    async with state.proxy() as data:
        data["country"] = country

    await GeneratePerson.select_gender.set()


@dp.message_handler(text="Украина", state=GeneratePerson.select_country)
async def ukraine(message: types.Message, state: FSMContext):
    country = message.text
    await message.answer("👤 Выберите пол вашей личности", reply_markup=gender_select)
    
    async with state.proxy() as data:
        data["country"] = country

    await GeneratePerson.select_gender.set()

@dp.message_handler(text="США", state=GeneratePerson.select_country)
async def usa(message: types.Message, state: FSMContext):
    country = message.text
    await message.answer("👤 Выберите пол вашей личности", reply_markup=gender_select)
    
    async with state.proxy() as data:
        data["country"] = country

    await GeneratePerson.select_gender.set()


@dp.message_handler(state=GeneratePerson.select_gender)
async def get_person(message: types.Message, state: FSMContext):
    country = await state.get_data("country")
    gender = message.text

    if country.get("country") == "Россия":
        person = Person(locale=Locale.RU)
    elif country.get("country") == "Украина":
        person = Person(locale=Locale.UK)
    elif country.get("country") == "США":
        person = Person(locale=Locale.EN)

    if gender == "Женский":
        name = person.full_name(gender=Gender.FEMALE)
    elif gender == "Мужской":
        name = person.full_name(gender=Gender.MALE)
    else:
        await message.answer("Пол не определен.")
        await state.finish()
    
    birthday = f"{r.randint(1, 30)}/{r.randint(1, 12)}/{r.randint(1980, 2015)}" # d.m.Y
    email = person.email()
    phone = person.telephone()

    height = person.height()
    weight = person.weight()
    eye_color = r.choice(["Синий", "Голубой", "Серый", "Зеленый", "Карий"])
    political_views = person.political_views()

    await message.answer(send(name, birthday, email, phone, height, weight, eye_color, political_views))

    await state.finish()