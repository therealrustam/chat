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
            margin: 50px 50px;
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
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    counter = 0
    while True:
        data = await websocket.receive_text()
        if data != "":
            counter += 1
            await websocket.send_json(f"{counter}. {data}")
        continue
