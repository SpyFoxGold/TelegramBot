import sqlite3
import datetime

#Создаёт новую таблицу в db
def SQL_createNewTable(NameOfUser, basename): #basename должен быть в str 'my_database.db'
    connection = sqlite3.connect(basename, check_same_thread=False)
    cursor = connection.cursor()

    NameOfUser = str(NameOfUser)
    basename = str(basename)

    Create = str('''CREATE TABLE IF NOT EXISTS ''') + str(NameOfUser) + str(''' (key INTEGER PRIMARY KEY, request TEXT NOT NULL, date TEXT NOT NULL)''')

    #print(Create)

    cursor.execute(Create)

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


# Example
    #   SQL_createNewTable('Botinok', 'my_database.db')
    #Создаёт таблицу ботинок в таблице my_database)


#Запись в userdata
def Add_Sketch_in_userdata(basename, UserNameBase,  request):
    connection = sqlite3.connect(basename, check_same_thread=False)
    cursor = connection.cursor()

    UserNameBase = str(UserNameBase)
    basename = str(basename)
    request = str(request)

    Create = 'INSERT INTO ' + str(UserNameBase) + ' (request, date) VALUES (?, ?)'

    cursor.execute(Create,(str(request),str(str(datetime.datetime.now())[:19])))


    connection.commit()
    connection.close()


#EXAMPLE Add_Sketch_in_table("SFG", "my_database.db", "Tesifychik")

def ListTableBase(database): #Выдаёт список всех таблиц в базе
  str(database)
  connection = sqlite3.connect(database)
  cursor = connection.cursor()

  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  A = cursor.fetchall()
  B=[]

 # Name = str("('SpyFoxGold',)")

  for i in range(0, len(A)):
      element = str(A[i])
      new_element = element[2:-3]
      B.append(new_element)

  connection.commit()
  connection.close()
  return(B)

  #запись в  users
def Add_Sketch_in_users(basename,username):
  if str(username) not in (ListTableBase(basename)):
      connection = sqlite3.connect(basename, check_same_thread=False)
      cursor = connection.cursor()

      username = str(username)
      basename = str(basename)

      Create = 'INSERT INTO ' + "Users" + ' (username, reg_date) VALUES (?, ?)'

      cursor.execute(Create,(str(username),str(str(datetime.datetime.now())[:19])))



      connection.commit()
      connection.close()
