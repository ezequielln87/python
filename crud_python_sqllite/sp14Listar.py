import sqlite3

conector = sqlite3.connect("conta.db")
cursor = conector.cursor()

sql = "select * from cadastro"
cursor.execute(sql)
dados = cursor.fetchall()

cursor.close()
conector.close()

for d in dados:
    print(d[0], d[1], d[2])

# print("Encontrados {} registros".format(len(dados)))
print(f"Encontramos{(len(dados))} registros")
