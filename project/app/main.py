# project/app/main.py


import logging
from app.api import ping, summaries  # updated
from app.db import init_db
from fastapi import FastAPI

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )  # new

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up ...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
