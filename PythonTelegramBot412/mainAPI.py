# python -m uvicorn mainAPI:app --reload

from fastapi import FastAPI
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db, engine
from app.models import User
from app import models
from myapp import ImageDownload, sqltablemode, DirectoryList
import config


# from app.schema import UserCreate, UserUpdate
app = FastAPI()

models.Base.metadata.create_all(bind=engine)



@app.get("/users/") #выдаёт список юзеров их id и их дату регистрации. таблица Users из main
def get_users():
    A = sqltablemode.ListTableBase('userdata.db') #Получили список всех юзеров
    B = sqltablemode.FirstRowList('userdata.db') #Получили список перовых строк из каждой таблицы из столбика date
    RES = 12 #Создаём json штуки по типу ("id": i, name":A[i], "registration":B[i])
    return B

#
# @app.get("/user/{user_id}") #выдаёт все реквесты юзера с датами из userdata по айди
# @app.get("/user/{username}") #выдаёт все реквесты юзера с датами из userdata по имени
#
# @app.get("/statistics/{type}") #Выдаёт информацию о запросах из Message_History
#


@app.post("/AddAnimal/{type}")
def add_photo(link,type: str):
    A = DirectoryList.AnimalList()
    if type in A:
        ImageDownload.DownloadImg(link, str(type))
        return ("Картинка загружена успешно")
    else: return('Существуют только слудующие типы:', A)

@app.post("/CreateAnimal/{type}")
def add_type(link,type, password: str):
    if password == config.PASSWORD:
        DirectoryList.CreateFolder(type)
        ImageDownload.DownloadImg(link, str(type))
        return ("Тип создан успешно")
    else: return("Пароль не совпадает")






