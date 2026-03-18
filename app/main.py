from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.web_interface.routes import generation


from app.core.config import get_settings

settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    #setup_logging()
    yield

app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan,
)

app.include_router(generation.router)