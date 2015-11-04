import random
resultado=[]
resultadoB=[]
print(25*' ','>>GERADOR DE NÚMEROS<<',4*'\n','\n>MEGASENA, LOTOFÁCIL, QUINA, LOTOMANIA, DUPLASENA, LOTOGOL, LOTECA e TIMEMANIA<\n')
taposta=str.lower(input('Vai gerar números para qual tipo de aposta? :'))
while(taposta!='megasena')and(taposta!='mega sena')and(taposta!='time mania')and(taposta!='timemania')and(taposta!='loto fácil')and(taposta!='lotofácil')and(taposta!='lotogol')and(taposta!='quina')and(taposta!='loto mania')and(taposta!='duplasena')and(taposta!='lotomania')and(taposta!='dupla sena')and(taposta!='loto gol')and(taposta!='loteca'):
    print('Vc digitou um tipo de aposta inválido!\n')
    taposta=str.lower(input('Vai a postar em qual tipo de aposta?'))
else:
    if(taposta=='megasena')or(taposta=='mega sena'):
        for cont in range(0,6):
            sorteio=random.randint(1,60)
            resultado.append(sorteio)
        print('\nOs números gerados aleatoriamente foram [',resultado,']')
    elif(taposta=='loto fácil')or(taposta=='lotofácil'):
        for cont in range(0,15):
            sorteio=random.randint(1,25)
            resultado.append(sorteio)
        print('\nOs números gerados aleatoriamente foram [',resultado,']')
    elif(taposta=='quina'):
        for cont in range(0,5):
            sorteio=random.randint(1,60)
            resultado.append(sorteio)
        print('\nOs números gerados aleatoriamente foram [',resultado,']')
    elif(taposta=='loto mania')or(taposta=='lotomania'):
        for cont in range(0,50):
            sorteio=random.randint(0,99)
            resultado.append(sorteio)
        print('\nOs números gerados aleatoriamente foram [',resultado,']')
    elif(taposta=='dupla sena')or(taposta=='duplasena'):
        for cont in range(0,6):
            sorteio=random.randint(0,51)
            resultado.append(sorteio)
        print('\nOs números gerados aleatoriamente foram [',resultado,']')
    elif(taposta=='loto gol')or(taposta=='lotogol'):
        for times in range(0,5):
            for times in range(0,1):
                sorteio=random.randint(0,4)
                sorteio2=random.randint(0,4)
            print('\nTime1=>',sorteio,'gols\nTime2=>',sorteio2,'gols')
    elif(taposta=='loteca'):
        for times in range(0,14):
            for placar in range(0,4):
                sorteio=random.randint(0,4)
                sorteio2=random.randint(0,4)
            print('\nTime1=>',sorteio,'gols\nTime2=>',sorteio2,'gols\n',12*'-')
    elif(taposta=='time mania')or(taposta=='timemania'):
        meutime=str.lower(input('qual seu time do coração? :'))
        for cont in range(0,10):
            sorteio=random.randint(1,80)
            resultado.append(sorteio)
        print('\nOs números gerados aleatoriamente foram [',resultado,'] e o time do coração é >>',meutime,'<<')

        
