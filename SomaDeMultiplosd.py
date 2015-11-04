cont=50
soma=0
while(cont>=1):
    num=float(input('Infome um número: '))
    if(num%3==0):
        soma=soma+num
    cont-=1
print('A soma dos números multiplos de 3 é',soma)
