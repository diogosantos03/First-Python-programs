while(True):
    num=int(input('Informe um número: '))
    if(num%2!=0):
        print('Número é impar')
    else:
        print('Número não é impar')
    if(num%3==0):
        print('Número é multiplo de 3')
    else:
        print('Número não é multiplo de 3')
    if(102%num==0):
        print('Número é divisor de 102')
    else:
        print('Número não é divisor de 102')
