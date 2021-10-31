import sys
sys.path.insert(0, r"C:/fastapi/ex5_sqlalchemy_core/")

from fastapi import APIRouter, HTTPException, status
from sqlalchemy import desc

from schemas import Cookie
from dabatase import engine, cookies

cookie_router = APIRouter()


@cookie_router.get("/cookie")
async def get():
    with engine.connect() as connection:
        result = connection.execute(
            cookies.select().order_by(
                desc(cookies.c.cookie_id)
                )
            )
        return [dict(row) for row in result]


@cookie_router.get("/cookie/{id}")
async def get_item(id: int):
    with engine.connect() as connection:
        result = connection.execute(
            cookies.select().where(
                cookies.c.cookie_id == id
                )
            ).first()
        if result:
            return result
        else:
            raise HTTPException(
                status_code=400,
                detail=f"No cookie found with id {id}"
            )


@cookie_router.post("/cookie", status_code=status.HTTP_201_CREATED)
async def create_cookie(cookie: Cookie):
    val = cookie.dict()
    del val["cookie_id"]
    with engine.connect() as connection:
        ins = cookies.insert().values(val)
        result = connection.execute(ins)
        return f"cookie created with id {result.inserted_primary_key[0]}"
