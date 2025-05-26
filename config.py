import os
from dotenv import load_dotenv

# pyhton-dotenv для настройки переменных окружения
# https://pypi.org/project/python-dotenv/

# предварительно создайте файл .env и поместите туда
# TOKEN=ВАШ_ТОКЕН

# берет переменные окружения из файла .env.
load_dotenv()

# переменные для tg_bot
TOKEN: str = os.getenv('TOKEN')
