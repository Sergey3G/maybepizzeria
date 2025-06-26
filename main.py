from fastapi import FastAPI

from database import Base, engine

from routers.users import router as users_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router)


@app.get("/")
async def root():
    return "root"
