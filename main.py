"""
Тестовое задание по созданию чата
посредстовом протокола WebSocket
между сервером и клиентом.
"""

import json

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="utf-8">
        <title>Чат - тестовое задание</title>
        <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: top;
            min-height: 100vh;
            color: #f0f8ff;
            background-color: #070217;
            font-size: 24px;
            font-family: 'Montserrat', sans-serif;
        }
        </style>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400&display=swap" rel="stylesheet">
    </head>
    <body>
        <h1>Чат</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Отправить</button>
        </form>
        <div id='messages'>
        </div>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('p')
                var result = JSON.parse(event.data)
                var content = document.createTextNode(
                    result.number + ". " + result.text)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(JSON.stringify({data: input.value}))
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    """
    Метод главной страницы с формой и чатом,
    который отправляет html шаблон.
    """
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    Метод обработки сообщения от клиента, присвоения ему порядкового номера
    и отправки итогового сообщения в чат на главную страницу в формате JSON.
    """
    await websocket.accept()
    counter = 0
    while True:
        data = await websocket.receive_json()
        text = data["data"]
        if text != "":
            counter += 1
            result = {"number": counter, "text": text}
            await websocket.send_json(result)
        continue
