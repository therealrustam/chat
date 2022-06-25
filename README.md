# Проект Chat

## Описание

Chat - это программа для создания соединения посредством протокола WebSocket между клиентом и сервером. Клиент может оправлять сообщения на сервер. Данное сообщение обрабатывается сервером, присваивается ему порядковый номер и отправляется в формате JSON клиенту на главную страницу.
Программа создана на основе фреймворка **FastAPI** языка программирования **Python**.

## Установка

Клонируйте новый репозиторий себе на компьютер.
Разверните в репозитории виртуальное окружение: в папке скачанного репозитория выполните команду: `python -m venv venv`.
Активируйте виртуальное окружение: `source venv/Scripts/activate`.
В виртуальном окружении установите зависимости: `pip install -r requirements.txt`.
Для запуска программы введите команду: `uvicorn main:app --reload`.

## Стек технологии

- anyio==3.6.1
- black==22.3.0
- click==8.1.3
- colorama==0.4.5
- fastapi==0.78.0
- flake8==4.0.1
- h11==0.13.0
- httptools==0.4.0
- idna==3.3
- importlib-metadata==4.2.0
- mccabe==0.6.1
- mypy-extensions==0.4.3
- pathspec==0.9.0
- platformdirs==2.5.2
- pycodestyle==2.8.0
- pydantic==1.9.1
- pyflakes==2.4.0
- python-dotenv==0.20.0
- PyYAML==6.0
- sniffio==1.2.0
- starlette==0.19.1
- tomli==2.0.1
- typed-ast==1.5.4
- typing_extensions==4.2.0
- uvicorn==0.18.1
- watchfiles==0.15.0
- websockets==10.3
- zipp==3.8.0

## Авторы

Вахитов Рустам
