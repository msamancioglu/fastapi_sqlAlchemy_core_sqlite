import sys
sys.path.insert(0, r"C:/fastapi/ex5_sqlalchemy_core/")

from fastapi import APIRouter, HTTPException, status
from sqlalchemy import desc, exc

from schemas import User
from dabatase import engine, users

user_router = APIRouter()

@user_router.get("/user")
async def get():
    with engine.connect() as connection:
        result = connection.execute(
            users.select().order_by(
                desc(users.c.user_id)
                )
            )
        return [dict(row) for row in result]


@user_router.get("/user/{id}")
async def get_user(id: int):
    with engine.connect() as connection:
        result = connection.execute(
            users.select().where(
                users.c.user_id == id
                )
            ).first()
        if result:
            return result
        else:
            raise HTTPException(
                status_code=400,
                detail=f"No cookie found with id {id}"
            )


@user_router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    val = user.dict()
    del val["user_id"]
    with engine.connect() as connection:
        try:
            ins = users.insert().values(val)
            result = connection.execute(ins)
        except exc.IntegrityError:
            print("yakaladım seni")
            raise HTTPException(
                status_code=400,
                detail=f"Username aready in use"
            )
            
        return f"user created with id {result.inserted_primary_key[0]}"
