def calcular_desconto():                    #7
    if valor <= 100:                        #2
        valor -= valor * 0.03               #3
        elif valor <= 500:                  #1
            valor -= valor * 0.10           #5
        elif valor <= 1000:                 #4
            valor -= valor * 0.20           #6
    return valor                            #8