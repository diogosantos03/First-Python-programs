cont=50
maior=0
impar=0
while(cont>=1):
    num=int(input('Informe um número: '))
    if(num%2!=0):
        impar+=1
        if(num>maior):
            maior=num
    cont-=1
if(impar==0):
    print('Não foram encontrados números ímpares')
else:
    print(maior,'é o maior número ímpar')
