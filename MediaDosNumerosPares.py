pare=100
soma=0
media=0
quant=0
a='Não foram lidos números pares'
num=int(input('Informe um número: '))
while(num!=pare):
    if(num%2==0):
        if(num==0):
            soma=soma
        else:
            soma+=num
            quant+=1
    else:
        a
    num=int(input('Informe um número: '))
if(soma==0):
    print(a)
else:
    print('a média dos números pares é:',soma/quant)
