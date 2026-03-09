import asyncio
from telegram import Bot

TOKEN = "8784169075:AAGzSdQtWTZl_trLs6N_Ta2U4jGgYX-I0j8"
CHAT_ID = -1003084692511

bot = Bot(token=TOKEN)

users = [
    "Гаевой",
    "Сеня",
    "Марат",
    "Анна",
    "Лёня",
    "Рогов",
    "Налсур",
    "Янееес",
    "даааааааааааааа)))))))))))",
    "нееееееееееееееет)))))))",
    "мипо",
    "алихааааан",
    "орлооооооооооов",
    "тимофееееей",
    "Артуууур",
    "Короообка",
    "Лобаааааааааас",
    "Шан уебище)",
    "Копытова",
    "Кнок сука жарит",
    "Андрей Манго",
    "Шкаф Миленя",
    "Мактрахер",
]

async def send_messages():
    while True:
        for user in users:
            await bot.send_message(chat_id=CHAT_ID, text=f"{user} ❤️")
            await asyncio.sleep(45)

asyncio.run(send_messages())
