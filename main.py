import time

from celery import Celery
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

celery = Celery(
    __name__,
    broker='redis://127.0.0.1:6379/0',
    backend='redis://127.0.0.1:6379/0',
    broker_connection_retry_on_startup=True
)


def call_background_task(message):
    time.sleep(10)
    print(f"Background Task called!")
    print(message)


@app.get("/")
async def hello_world(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(call_background_task, message)
    return {'message': 'Hello World!'}