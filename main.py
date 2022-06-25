"""
Тестовое задание по созданию чата
посредстовом протокола WebSocket
между сервером и клиентом.
"""

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="utf-8">
        <title>Чат</title>
        <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            color: #f0f8ff;
            background-color: #070217;
            font-size: 20px;
            font-family: "Helvetica", Times, serif;
        }
        </style>
    </head>
    <body>
        <h1>Чат тестового задания</h1>
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
                var content = document.createTextNode(JSON.parse(event.data))
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
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
        data = await websocket.receive_text()
        if data != "":
            counter += 1
            await websocket.send_json(f"{counter}. {data}")
        continue
