# example-tgbot

Ranepa telegram bot for education (computer science)

## Установка

### Запуск проекта из исходника

1. Для запуска проекта стяните его с помощью `git clone`

2. Перейдите в каталог проекта и создайте изолированную среду. Например, `.venv`

```
python3 -m venv .venv
```

3. Запустите среду и установите зависимости
   
```
pip install -r requirements.txt
```

4. Полученный токен в [BotFather](https://t.me/BotFather) вставить в созданный файл `.env`

```
TOKEN=<ВАШ ТОКЕН>
```

5. Для запуска проекта введите в консоли

```
python3 main.py
```
### Запуск docker-контейнера

1. Для запуска проекта в контейнере стяните его с помощью `git clone`. Проект содержит `Dockerfile` и `docker-compose.yml`

2. Полученный токен в [BotFather](https://t.me/BotFather) вставить в созданный файл `.env`. На удаленном сервере это можно сделать с помощью редакторов `nano` или `vim`.

```
TOKEN=<ВАШ ТОКЕН>
```

С помощью команды `echo`.

```
echo "TOKEN=<ВАШ ТОКЕН>" > .env
```

3. Перейдите в каталог проекта и запустите команду сборки контейнера `example-tgbot:vX`, где X – текущая версия проекта.

```
docker build -t <ВАШ КОНТЕЙНЕР>:v<ВЕРСИЯ> .
```
3. Для запуска контейнера в фоновом режиме используйте команду

```
docker run -d -e .env <ВАШ КОНТЕЙНЕР>:v<ВЕРСИЯ>
```

Проверить состоятние запущенного контейнера для `docker`

```
docker ps
```

4. Для автоматизированной сборки нескольких контейнеров воспользуйтесь `docker-compose`. При запуске на удаленном сервере `docker-compose` будет перезапускать контейнеры автоматически!

```
docker-compose up --build -d
```

Проверить состоятние запущенного контейнера для `docker-compose`

```
docker-compose ps
```

5. Если вы хотите остановить контейнер `docker`

```
docker stop <ID-контейнера>
```

Для удаления контейнера

```
docker rm <ID-контейнера>
```

Если вы хотите остановить `docker-compose`

```
docker-compose down
```

Перезапустить контейнеры

```
docker-compose restart
```

## Материал

* Дополнительный гайд по aiogram https://mastergroosha.github.io/aiogram-3-guide/quickstart/
* Дополнительный гайд по асинхронному бэкенду https://habr.com/ru/companies/kts/articles/598575/
* Для создания бота необходимо получить token в telegram https://t.me/BotFather
* Бот принимает команды, например /start. Создадим хендлер - обработчик сообщений, и будем возвращать сообщение, указанное в функции подробнее о конструкции async/await - https://docs-python.ru/tutorial/sintaksis-async-await-python/
* Запуск процесса поллинга новых апдейтов. Существует 2 способа получить уведомления:
  * `webhook` — инициатором запроса выступает Телеграм. Когда пользователь пишет боту, Телеграм делает запрос на URL, который вы установите с помощью метода setwebhook.
  * `long polling` — инициатором является ваше приложение. Оно обращается к Telegram API и получает уведомления или ожидает, если уведомлений нет.
* pyhton-dotenv для настройки переменных окружения https://pypi.org/project/python-dotenv/
* Дополнительный материал про создание Docker-контейнера и запуск бота https://habr.com/ru/articles/823714/
