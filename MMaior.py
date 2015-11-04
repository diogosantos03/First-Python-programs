cont=50
quant=0
while(cont>=1):
    num=int(input('Informe um número: '))
    if(num>=0):
        if(num%2!=0):
            quant+=1
            if(quant==1):
                maior=num
            else:
                if(num>maior):
                    maior=num
    else:
        break
    cont-=1
if(num<0):
    print('vc não poderia ter informado um num negativo!!')
if(maior==0):
    print('Não foram encontrados números ímpares')
else:
    print(maior,'é o maior número ímpar')
