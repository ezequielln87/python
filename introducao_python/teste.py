def listEscolha(escolha):
    for index, item in enumerate(escolha):
        conteudo = [int((index + 1)), str(item)]
        imprime.append(conteudo)
    return imprime


escolha = ['Big Mac', 'McFlurry', 'McChicken', 'Big Tasty']

print('Escolha uma opção:')
imprime = []
resultado = listEscolha(escolha)

print(resultado)
pesquisa = int(input('Qual o número do pedido?'))
