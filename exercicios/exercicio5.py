import pandas as pd


def minha_funcao(valor):
    for i, c in enumerate(valor):
        if c.lower() == 'a' or c.lower() == 'e':
            print('possui', c, i)
        else:
            print('nao eh vogal')


letra = input("letra")
resultLetra = minha_funcao(letra)
print(resultLetra)
