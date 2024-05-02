# python -m uvicorn mainAPI:app --reload

from fastapi import FastAPI
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db, engine
from app.models import User
from app import models
from myapp import ImageDownload
#, sqltablemode, DirectoryList

# from app.schema import UserCreate, UserUpdate
app = FastAPI()

models.Base.metadata.create_all(bind=engine)



# @app.get("/users/") #выдаёт список юзеров их id и их дату регистрации. таблица Users из main
#
# @app.get("/user/{user_id}") #выдаёт все реквесты юзера с датами из userdata
# @app.get("/user/{username}") #выдаёт все реквесты юзера с датами из userdata
#
# @app.get("/statistics/{type}") #Выдаёт информацию о запросах из Message_History
#


@app.post("/AddAnimal/{type}")
def add_photo(link,type: str):
    ImageDownload.DownloadImg(link, str(type))
    return ("Картинка загружена успешно")

# @app.post("/CreateAnimal/{type}")








# @app.get("/users/")
# def get_all_users(db: Session = Depends(get_db)):
#     return sqltablemode.ListTableBase('my_database.db')    #остановился тут
#
# @app.get("/users/{user_id}")
# def get_user_by_username(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == user_id).first()
#     if user:
#         return user
#     raise HTTPException(status_code=404, detail="User not founde")
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.post("/Cats")
# def add_photo(link: str):
#     ImageDownload.DownloadImg(link, "Cats")
#     return ("Картинка загружена успешно")
#
# @app.post("/Dogs")
# def add_photo(link: str):
#     ImageDownload.DownloadImg(link, "Dogs")
#     return ("Картинка загружена успешно")
