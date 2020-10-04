def Read():
    sql = "select * from cadastro "
    cursor.execute(sql)
    dados = cursor.fetchall()
    cursor.close()
    conector.close()
for d in dados:
    print(d[0], d[1], d[2])

def UPdate(Cod,new):
    cursor.execute("""
    UPDATE cadastro
    SET idade = ?
    where codigo = ?
    """, (new,Cod))
    conector.commit()

def ExcluiCliente(Cod):
    sql = "delete from cadastro where codigo = :param"
    cursor.execute(sql, {'param':Cod})
    conector.commit()
    return "Cliente {} Excluído".format(Cod)
