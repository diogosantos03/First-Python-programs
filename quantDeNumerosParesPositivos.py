cont=5
quant=0
while(cont>=1):
    num=float(input('Informe um número: '))
    if(num%2==0):
        if(num>0):
            quant+=1
    cont-=1
print('A quantidade de números pares e positivos é',quant)
