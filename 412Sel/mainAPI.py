#python -m uvicorn mainAPI:app --reload
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from typing import Union
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


    
app = FastAPI()








from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schema import UserCreate, UserUpdate


@app.get("/users/")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/users/{user_id}")
def get_user_by_username(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not founde")


















'''
#тест ниже

class BaseUsers(db.model):
    __abstract__=True
    __table_name__ = 'my_database.db'
    id= db.Column(db.Integer)
    username = db.Column(db.String)
    request = db.Column(db.String)

class User(BaseUsers):
    __table_name__ = 'my_database.db'
    id = db.Column(db.Integer, primary_key=True)

@app.get("/itemz/{item_id}")
def read_root():
    return {User.id(1)}

#тест выше
'''



@app.get("/")
def read_root():
    return {"Hello": "World"}

async def idz(z):
    cursor.execute('SELECT username, request, id FROM Users WHERE id == ?', (z,) )
    results = cursor.fetchall()
    # Выводим результаты
    for user in results:
        a=user
    #разделение строки на пункты
    id=a[2]
    username=a[0]
    request=a[1]
    print(id, username, request)
    return(id)

async def usernamez(z):
    cursor.execute('SELECT username, request, id FROM Users WHERE id == ?', (z,) )
    results = cursor.fetchall()
    # Выводим результаты
    for user in results:
        a=user
    #разделение строки на пункты
    id=a[2]
    username=a[0]
    request=a[1]
    print(id, username, request)
    return(username)

async def requestz(z):
    cursor.execute('SELECT username, request, id FROM Users WHERE id == ?', (z,) )
    results = cursor.fetchall()
    # Выводим результаты
    for user in results:
        a=user
    #разделение строки на пункты
    id=a[2]
    username=a[0]
    request=a[1]
    print(id, username, request)
    return(request)

@app.get("/items/{item_id}")
async def read_item(item_id: int, username: Union[str, None] = None):
    id=await idz(item_id)
    username=await usernamez(item_id)
    # item.get(item_id)   Пример обращения к бд через модели

    request=await requestz(item_id)
    return {"item_id": id, "username": username, "request": request}