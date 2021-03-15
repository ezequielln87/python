import sp13_ClassConta

conta1 = sp13_ClassConta.Conta('Joao', 1)
conta1.Depositar(200.0)
print(conta1.getCliente(), ' - ', conta1.Saldo())

conta2 = sp13_ClassConta.Conta('Maria', 2)
conta2.Depositar(200.0)
print(conta2.getCliente(), ' - ', conta2.Saldo())

valor_transfere = int(input('Qual o valor que deseja transferir de João para Maria?'))
print('Transferido ', valor_transfere, ' reais da conta do Joao para Maria')
conta1.Transferencia(conta2, valor_transfere)

print('Resultado na conta de Maria')
print(conta2.Saldo())

print('Resultado na conta de Joao')
print(conta1.Saldo())