from fastapi import FastAPI

from api.v1 import notifications
from models.queues import get_queues_list
from db.utils import init_queues
import uvicorn as uvicorn


app = FastAPI(
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)


@app.on_event('startup')
async def create_queues_if_not_exists():
    init_queues(queues_list=get_queues_list())


app.include_router(notifications.router, prefix='/api/v1')

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=7000
    )
