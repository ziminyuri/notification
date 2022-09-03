from fastapi import FastAPI

from api.v1 import notifications
from models.queues import get_queues_list
from db.utils import init_queues


app = FastAPI(
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)


@app.on_event('startup')
async def create_queues_if_not_exists():
    init_queues(queues_list=get_queues_list())


app.include_router(notifications.router, prefix='/api/v1')
