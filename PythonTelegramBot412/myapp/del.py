# importing sqlite module
import sqltablemode
import sqlite3

# create connection to the
# database geek
connection = sqlite3.connect('userdata.db')

# drop table
connection.execute("DROP TABLE SpyFoxGold")

print("data dropped successfully")

# close the connection
connection.close()

#print(sqltablemode.ListTableBase('userdata.db'))
