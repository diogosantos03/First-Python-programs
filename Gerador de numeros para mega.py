import random
resultado=[]
print('\nO sorteio será de 1 até o número que você digitar!\n')
num=int(input('Digite um número: '))
while(num<6)or(num>60):
    if(num<6):
        print('Informe um número de 6 a 60, para que seja sorteado os 6 números para seu jogo!')
    elif(num>60):
        print('Informe um número de 6 a 60, para que seja sorteado os 6 números para seu jogo!')
    num=int(input('Digite um número: '))
else:
    for cont in range(0,6):
        sorteio=random.randint(1,num)
        resultado.append(sorteio)
    print('Os números sorteados foram [',resultado,']')
