import asyncio
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from buttons import main_buttons,school_buttons

bot = Bot(token="8984302315:AAEsFPi5pCOkeVTAT2hcY6cUCdSlnxH6ff4")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Assalomu alaykum! Xush kelibsiz !!!",
                        reply_markup= await main_buttons()
                        )
@dp.message(F.text == "maktab darsliklari")
async def reaction_to_school_lessons(message:Message):
    await message.answer("Sinf tanlang!",reply_markup=await school_buttons())

@dp.message(F.text == "Go Back")
async def go_back(message:Message):
    await message.answer("Asosiy sahifa",reply_markup=await main_buttons())


@dp.message(Command("help"))
async def help(message:Message):
    await message.answer("Kechirasz yordam bera olmayman !!!")

@dp.message(Command("Nmagap"))
async def nma_gap(message:Message):
    await message.answer("Tinchlik")




async def main():
    await dp.start_polling(bot)

asyncio.run(main())