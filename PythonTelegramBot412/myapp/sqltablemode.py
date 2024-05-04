import sqlite3
import datetime
import json
#//////////////////////////////////////ПЕРЕДЕЛАТЬ ВСЁ
#Нужно: Добавить строку в database.db/users, если такого id нет
#Нужно: Добавить строку в database.db/messages, если написано сообщение
#Запись в userdata


def UserListFromUsers(): #Выдаёт список никнеймов из таблицы Users
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    a= cursor.execute('SELECT username from Users')
    list = a.fetchall()
    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()
    res = []
    for i in range(0,len(list)):
        d = str(list[i])[2:-3]
        res.append(d)



    return(res)

def Add_User(username):
    A = UserListFromUsers()
    if username not in A:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        cursor.execute('INSERT INTO Users (username, registration_date) VALUES (?,?)', (username, str(str(datetime.datetime.now())[:19])))

        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()


def username_to_id(username):
    username = str(username)
    if username in UserListFromUsers():
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Добавляем нового пользователя
        a = cursor.execute('SELECT * from Users WHERE username = ?',(username,))
        list = a.fetchall()
        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()
        c = str(list[0])
        end = -(len(c)-2)
        res = str(c)[1:end]
        return(res)
    else: return("User not in base")

def Add_Message(username, text):
    text = str(text)
    username = str(username)
    if username in UserListFromUsers():
        # Устанавливаем соединение с базой данных
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        user_id = username_to_id(username)

        # Создаем таблицу Users
        cursor.execute('INSERT INTO Messages (user_id,	text,	date) VALUES (?, ?,?)', (user_id, text, str(str(datetime.datetime.now())[:19])))

        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()
    else: return("User not in base")




##JSON Moments

def json_users():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    a = cursor.execute('SELECT * from Users')
    list = a.fetchall()
    # Сохраняем изменения и закрываем соединение

    dataALL={}


    for i in range(0,len(list)):
        data = {
            "id": list[i][0],
            "name": list[i][1],
            'registration_date': list[i][2],
        }
        content = str('user_'+str(i+1))
        dataALL[content] = data
        #print(data)
        #dataALL = dataALL + json.dumps(data,indent=4) + n


    connection.commit()
    connection.close()
    return dataALL


def json_user_messages_id(id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    a = cursor.execute('SELECT * from Messages WHERE user_id=?',(id,))
    list = a.fetchall()
    RES={}#{}

    for i in range(0,len(list)):
        data = {"text": list[i][2],
            "date": list[i][3]
        }
        content = str('message_'+str(i+1))
        RES[content] = data



    connection.commit()
    connection.close()
    return(RES)



def statistics_values_list():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    a = cursor.execute('SELECT * from Messages')
    list = a.fetchall()

    RES={}#{}

    for i in range(0,len(list)):
        data = {"text": list[i][2]
        }
        content = str('message_'+str(i+1))
        RES[content] = data



    connection.commit()
    connection.close()
    return(RES)
