# class Pessoa:
#     def _init_(self, nome, telefone):
#         self.nome = nome
#         self.telefone = telefone
# -------------------------------------------
# class Queue:
#     def _int_(self):
#         self.q = []
#
#     def isEmpty(self):
#         return (len(self.q)) == 0)
#
#     def enqueue(self, item):
#         return self.q.append(item)
#
#     def dequeue(self):
#         return self.q.pop(0)

class Conta:
    def __init__(self, nome, numero):
        self.cliente = nome
        self.num = numero
        self.saldo = 0.0

    def Saldo(self):
        return self.saldo

    def getCliente(self):
        return self.cliente

    def Depositar(self, valor):
        self.saldo += valor

conta1 = Conta('Joao', 1)
conta1.Depositar(100.0)
print(conta1.saldo)
print(conta1.getCliente())

conta2 = Conta('Maria', 2)
conta2.Depositar(200.0)
print(conta2.Saldo())
print(conta2.getCliente())
