import random
resultado=[]
print('\nGERAR NÚMEROS PARA A MEGA SENA, LOTO FÁCIL OU QUINA!\n')
taposta=str.lower(input('Vai gerar números para qual sorteio? :'))
while(taposta!='mega')and(taposta!='mega sena')and(taposta!='loto fácil')and(taposta!='quina')and(taposta!='loto'):
    print('Vc digitou um tipo de aposta inválido!\n')
    taposta=str.lower(input('Vai a postar em qual sorteio?'))
else:
    if(taposta=='mega')or(taposta=='mega sena'):
        for cont in range(0,6):
            sorteio=random.randint(1,60)
            resultado.append(sorteio)
        print('Os números sorteados foram [',resultado,']')
    elif(taposta=='loto fácil')or(taposta=='loto'):
        for cont in range(0,15):
            sorteio=random.randint(1,60)
            resultado.append(sorteio)
        print('Os números sorteados foram [',resultado,']')
    elif(taposta=='quina'):
        for cont in range(0,5):
            sorteio=random.randint(1,60)
            resultado.append(sorteio)
        print('Os números sorteados foram [',resultado,']')
