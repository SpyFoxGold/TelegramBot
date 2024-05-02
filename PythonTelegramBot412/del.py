import sqlite3
from myapp import sqltablemode

def FirstRowList(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    database = str(database)
    A = []
    TableList = sqltablemode.ListTableBase(database)
    for i in range(len(TableList)):
        table = str(TableList[i])
        cursor.execute("SELECT * FROM " + str(table))
        row = cursor.fetchone()
        A.append(row)

    connection.commit()
    connection.close()
    return(A)



print(FirstRowList('userdata.db'))
