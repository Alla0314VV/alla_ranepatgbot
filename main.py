# version 0.1.0
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from config import TOKEN

# Экземпляры бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Бот принимает команды, например /start.
# Создадим хендлер - обработчик сообщений, и будем возвращать сообщение
@dp.message(Command("start"))
async def process_start_command(message):
    await message.answer("Привет!")

# Эхо-ответ на любое сообщение
# Декораторы @dp.message() необходимы для получения сообщения и отправки результата функции в телеграм
@dp.message()
async def echo_message(message):
    await message.answer(message.text)

# Функция запуска бота
# Запуск процесса поллинга новых апдейтов. Существует 2 способа получить уведомления:
# webhook — инициатором запроса выступает Телеграм. Когда пользователь пишет боту, Телеграм делает запрос на URL,
# который вы установите с помощью метода setwebhook.
# long polling — инициатором является ваше приложение.
# Оно обращается к Telegram API и получает уведомления или ожидает, если уведомлений нет.
async def main():
    await dp.start_polling(bot)

# Скрипт инициализации
# Подробнее про асинхронные функции и асинхронный ввод-вывод по ссылке
# https://habr.com/ru/articles/667630/
if __name__ == "__main__":
    asyncio.run(main())
