import sqlite3

db = sqlite.connect("fighters.db")
cursor = db.cursor()
sql = "SELECT * from fighter;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)

db.close()