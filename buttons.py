from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


async def main_buttons():
    markup = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text="maktab darsliklari",
                               style = "success"),
                KeyboardButton(text= "badiiy adabiyot",
                               style = "success")
            ],
            [
                KeyboardButton(text = "IT Course",
                               style = "primary"),
                KeyboardButton(text="IELTS Course",
                               style = "primary")
            ],
            [
                KeyboardButton(text = "Send location",request_location=True,style = "danger"),
                KeyboardButton(text = "Send contact",request_contact=True,style = "danger")
            ]

        ],
        resize_keyboard=True
    )
    return markup
async def school_buttons():
    buttons = []
    for i in range(1,12):
        buttons.append([KeyboardButton(text=f"📔 {i}-sinf darsliklari")])
    buttons.append([KeyboardButton(text="Go Back")])
    return ReplyKeyboardMarkup(keyboard=buttons,resize_keyboard=True)