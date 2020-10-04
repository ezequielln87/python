def BuscaSeq(list, item):
    pos =0
    x= False

    while pos<len(list) and not x:
        if list[pos]== item:
            x= True
        else:
            pos = pos +1
    return x


lista = [4, 6, 8, 12, 1, 5, 7]
teste = len(lista)
# print(teste)

pesquisa = int(input("Qual valor deseja pesquisar?"))
resultado = (BuscaSeq(lista, pesquisa))

if resultado == True:
    print('Sim, a lista possui o valor')
else:
    print('Valor não encontrado na lista')

(BuscaSeq(lista, pesquisa))
# print(BuscaSeq(lista, 8))
# print(BuscaSeq(lista, 13))
