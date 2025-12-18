import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import FSInputFile


API_TOKEN = '8158621347:AAGzwSY69Wv7zQcLH972f0zq2zgJ9BB2oyI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("я ботик")


    builder = ReplyKeyboardBuilder()


    builder.add(types.KeyboardButton(text="Показать котика"))
    builder.add(types.KeyboardButton(text="Показать мем"))
    builder.add(types.KeyboardButton(text="о нас"))

    builder.adjust(2, 1)


    await message.answer(
        "Выберите пункт меню:",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )

@dp.message(F.text == "о нас")
async def send_about(message: types.Message):
    await message.answer("секретная разработка нейросеть разработка мгту")

@dp.message(F.text == "Показать котика")
async def send_cat_image(message: types.Message):

    try:
        photo_file = FSInputFile("pic2.jpg")
        await message.answer_photo(
            photo=photo_file,
            caption="я грр"
        )
    except Exception as e:
        await message.answer(f"Ошибка отправки фото: {e}")

@dp.message(F.text == "Показать мем")
async def send_meme_image(message: types.Message):

    try:
        photo_file = FSInputFile("pic.jpg")
        await message.answer_photo(
            photo=photo_file,
            caption="76567576567 лайков"
        )
    except Exception as e:
        await message.answer(f"Ошибка отправки фото: {e}")

async def main():

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
