from fastapi import FastAPI

from api.v1 import notifications


app = FastAPI(
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)

app.include_router(notifications.router, prefix='/api/v1')
