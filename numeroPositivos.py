a = int (input('Informe um número'))
b = int (input('Informe um número'))
c = int (input('Informe um número'))
while(a>0)and(b>0)and(c>0):
    if (a > b) and (a > c):
        print(a)
    elif (b > a) and (b > c):
        print(b)
    else:
        print(c)
    a = int (input('Informe um número:'))
    b = int (input('Informe um número:'))
    c = int (input('Informe um número:'))
print('vc digitou um número negativo!')
