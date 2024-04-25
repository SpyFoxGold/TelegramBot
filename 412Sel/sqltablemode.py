import sqlite3

#Создаёт новую таблицу в db
def SQL_createNewTable(NameOfUser, basename): #basename должен быть в str 'my_database.db'
    connection = sqlite3.connect(basename, check_same_thread=False)
    cursor = connection.cursor()

    NameOfUser = str(NameOfUser)
    basename = str(basename)

    Create = str('''CREATE TABLE IF NOT EXISTS ''') + str(NameOfUser) + str(''' (id INTEGER PRIMARY KEY, username TEXT NOT NULL, request INTEGER)''')

    print(Create)

    cursor.execute(Create)

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


# Example
    #   SQL_createNewTable('Botinok', 'my_database.db') 
    #Создаёт таблицу ботинок в таблице my_database)



def Add_Sketch_in_table(UserNameBase, basename, message):
    connection = sqlite3.connect(basename, check_same_thread=False)
    cursor = connection.cursor()

    UserNameBase = str(UserNameBase)
    basename = str(basename)
    message = str(message)

    Create = 'INSERT INTO ' + str(UserNameBase) + ' (username, request) VALUES (?, ?)' 

    cursor.execute(Create,(str(UserNameBase),str(message)))


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

  Name = str("('SpyFoxGold',)")

  for i in range(0, len(A)):
      element = str(A[i])
      new_element = element[2:-3]
      B.append(new_element)

  connection.commit()
  connection.close()
  return(B)