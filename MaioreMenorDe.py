while(True):
    numA=float(input('informe um número: '))
    numB=float(input('informe um número: '))
    numC=float(input('informe um número: '))
    if(numA>numB)and(numA>numC):
        maior=numA
    elif(numB>numA)and(numB>numC):
        maior=numB
    else:
        maior=numC
    if(numA<numB)and(numA<numC):
        menor=numA
    elif(numB<numA)and(numB<numC):
        menor=numB
    else:
        menor=numC
    print('o maior é',maior,'e o menor é',menor)
