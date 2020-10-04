def bubbleSort(list):
    n = len(lista)
    for j in range(n - 1):
        for i in range(n - 1):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                print(list)


lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(lista)
print(lista)