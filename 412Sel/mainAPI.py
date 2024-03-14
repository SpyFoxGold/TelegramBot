#python -m uvicorn mainAPI:app --reload

from typing import Union
import sqlite3
from fastapi import FastAPI

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()



app = FastAPI()


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