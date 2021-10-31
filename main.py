from fastapi import FastAPI
import uvicorn
from routers.cookies import cookie_router
from routers.users import user_router

app = FastAPI()

app.include_router(cookie_router)
app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
