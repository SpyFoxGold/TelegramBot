import sqlite3
#id,username, request




# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#cursor.execute('INSERT INTO Users (username, request) VALUES (?, ?)', ('newuser', 'newuser@example.com'))


# Выбираем всех пользователей
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

# Выводим результаты
for user in users:
  print(user)



# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()