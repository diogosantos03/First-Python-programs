import random
num=int(input('Informe um número: '))
while(num<6)or(num>60):
    if(num<6):
        print('Informe um número de 6 a 60, para que seja sorteado os 6 números para seu jogo!')
    elif(num>60):
         print('Informe um número de 6 a 60, para que seja sorteado os 6 números para seu jogo!')
    num=int(input('Informe um número: '))
else:
    diogo1=random.randint(1,num)
    diogo2=random.randint(1,num)
    diogo3=random.randint(1,num)
    diogo4=random.randint(1,num)
    diogo5=random.randint(1,num)
    diogo6=random.randint(1,num)
    print('\nO primeiro número sorteado:',diogo1)
    print('O segundo número sorteado:',diogo2)
    print('O terceiro número sorteado:',diogo3)
    print('O quarto número sorteado:',diogo4)
    print('O quinto número sorteado:',diogo5)
    print('O sexto número sorteado:',diogo6)
    
