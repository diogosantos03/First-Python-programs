while(True):
    numA=float(input('informe um número: '))
    numB=float(input('informe um número: '))
    numC=float(input('informe um número: '))
    if(numA>numB)and(numA>numC):
        print(numA)
    elif(numB>numA)and(numB>numC):
        print(numB)
    else:
        print(numC)
