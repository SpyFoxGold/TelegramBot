import sqlite3
#id,username, request




# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#cursor.execute('INSERT INTO Users (username, request) VALUES (?, ?)', ('newuser', 'newuser@example.com'))


# Выбираем всех пользователей
z=24
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



# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()