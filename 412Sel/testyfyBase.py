import sqlite3

def ListTeable(database):
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