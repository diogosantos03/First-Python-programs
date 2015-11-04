while(True):
    numA=float(input('informe um número: '))
    numB=float(input('informe um número: '))
    numC=float(input('informe um número: '))
    if(numA>numB)and(numA>numC):
        if(numB>numC):
            print(numC,numB,numA)
        else:
            print(numB,numC,numA)
    elif(numB>numA)and(numB>numC):
        if(numA>numC):
            print(numC,numA,numB)
        else:
            print(numA,numC,numB)
    elif(numC>numA)and(numC>numB):
        if(numA>numB):
            print(numB,numA,numC)
        else:
            print(numA,numB,numC)
