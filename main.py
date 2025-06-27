from fastapi import FastAPI
import asyncio

from database import Base, engine

from routers.users import router as users_router


app = FastAPI()

app.include_router(users_router)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return "root"
