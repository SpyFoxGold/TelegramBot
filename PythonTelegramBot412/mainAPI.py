# python -m uvicorn mainAPI:app --reload

from fastapi import FastAPI
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from myapp import ImageDownload, sqltablemode, DirectoryList
import config




app = FastAPI()





@app.get("/users/") #выдаёт список юзеров их id и их дату регистрации. таблица Users из main
def get_users():
    return(sqltablemode.json_users())


@app.get("/user/{user_id}") #выдаёт все реквесты юзера с датами из userdata по айди
def get_user_id_messages(id:int):
    return(sqltablemode.json_user_messages_id(id))




@app.get("/statistics/{type}") #Выдаёт информацию о запросах
def get_statisctics_type(type:str):
    RES = {}
    list = DirectoryList.AnimalList()
    for j in range(0, len(list)):
        RES[list[j]] = {0}
    RES['Other'] = {0}

    a = sqltablemode.statistics_values_list()
    for i in range(0,len(a)):
        b = a.get('message_'+str(i+1))
        c = b.get('text')

        if c in list:
            a1 = str(RES.get(c))
            a1 = int(a1[1:-1])
            a1+=1
            RES[c]={a1}
        else:
            a1 = str(RES.get('Other'))
            a1 = int(a1[1:-1])
            a1+=1
            RES['Other']={a1}

    n_list = list
    n_list.append('Other')
    if type == "all":
        return(RES)
    elif type in n_list:
        return({type : RES[type]})
    else: return("Поддерживаются только следующие типы:", n_list)




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
