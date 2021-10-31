from pydantic import BaseModel
from typing import Optional

from datetime import datetime

class Cookie(BaseModel):
    cookie_id: Optional[int]
    cookie_name: str
    cookie_recipe_url: str
    cookie_sku: Optional[str]
    quantity: Optional[int]
    unit_cost: Optional[float]

class User(BaseModel):
    user_id: Optional[int]
    username: str
    email_address: str
    phone: str
    password: str
    created_on: Optional[datetime]
    updated_on: Optional[datetime]


#  Column('user_id', Integer(), primary_key=True),
#  Column('username', String(15), nullable=False, unique=True),
#  Column('email_address', String(255), nullable=False),
#  Column('phone', String(20), nullable=False),
#  Column('password', String(25), nullable=False),
#  Column('created_on', DateTime(), default=datetime.now),
#  Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)