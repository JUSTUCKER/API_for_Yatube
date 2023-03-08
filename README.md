# API для Yatube

Данное API позволяет использовать функционал проекта Yatube* без сайта. 

**Yatube - социальная сеть для блогеров.*


## Установка

Клонировать репозиторий:
```bash
git clone https://github.com/JUSTUCKER/api_final_yatube.git
```

Перейти в папку с проектом:
```bash
cd api_final_yatube/
```

Создать виртуальное окружение:
```bash
python3 -m venv env
```

Активировать виртуальное окружение:
```bash
# для OS Lunix и MacOS
source venv/bin/activate
```
```bash
# для OS Windows
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
python3 manage.py migrate
```

Запустить проект:
```bash
python3 manage.py runserver
```
## Примеры запросов к API

#### Получение токена:

Адрес запроса:
```http
POST /api/v1/jwt/create/
```

Тело запроса:
```http
{
  "username": "string",
  "password": "string"
}
```

*Пример ответа:*
```http
{
  "refresh": "string",
  "access": "string"
}
```
**При отправке дальнеших запросов - передай полученный из поля "access" токен в заголовок Authorization: Bearer.*

#### Получение публикации:

Адрес запроса:
```http
GET /api/v1/posts/{id}/
```

*Пример ответа:*
```http
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

#### Создание нового поста:

Адрес запроса:
```http
POST /api/v1/posts/
```

Тело запроса:
```http
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

*Пример ответа:*
```http
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
## Документация проекта

[Переходи при запущенном проекте](http://127.0.0.1:8000/redoc/)


## Автор

- [@JUSTUCKER](https://github.com/JUSTUCKER)
