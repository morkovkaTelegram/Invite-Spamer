import telegram
import random
import string
import asyncio
import os
from datetime import timedelta, datetime

# установите свой токен из @BotFather
TOKEN = 'YOUR_BOT_TOKEN'

# создаем сессию бота
bot = telegram.Bot(token=TOKEN)

# функция для создания случайной строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# указываем chat_id чата, в котором будут созданы приглашения
chat_id = int(input("Введите id чата(Вместе с -100): "))

# количество приглашений, которые нужно создать
num_invites = int(input("Введите кол-во создаваемых ссылок: ")) 

# задержка между созданием приглашений в секундах
delay = float(input("Введите задержку между созданием ссылок в секундах: "))

# указываем username пользователя, которому нужно отправить приглашения (можно взять из @username_to_id_bot)
user_id = 'YOUR_ID'

async def create_invites():
    # создаем заданное количество приглашений и отправляем их пользователю в личные сообщения
    for i in range(num_invites):
        invite_link = await bot.create_chat_invite_link(chat_id=chat_id, member_limit=1) #member limit - Максимальное количество пользователей которые могут присоединиться 1-99999
        invite_string = f"{invite_link.invite_link}"
        await bot.send_message(chat_id=user_id, text=invite_string, disable_web_page_preview=True)
        await asyncio.sleep(delay)

# создаем цикл событий и запускаем асинхронную функцию для создания приглашений
loop = asyncio.get_event_loop()
loop.run_until_complete(create_invites())
print("Скрипт успешно завершен!")
