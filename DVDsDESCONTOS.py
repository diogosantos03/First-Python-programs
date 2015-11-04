tlanc=4
tcomum=3
valorC=0
valorL=0
desconto=(8/100)
cliente=str.lower(input('Cliente comum ou especial? '))
quantfilme=int(input('Vai alugar quantos filmes? '))
if(cliente=='comum'):
    if(quantfilme==1):
        tfilme=str.lower(input('O tipo de filme é lançamento ou comum? '))
        tdvd=str.lower(input('O tipo de dvd é simples ou duplo? '))
        if(tfilme=='lançamento'):
            if(tdvd=='simples'):
                valorL=tlanc
            elif(tdvd=='duplo'):
                valorL=tlanc*2
            else:
                print('Não temos essa opção!')
        elif(tfilme=='comum'):
            if(tdvd=='simples'):
                valorC=tcomum
            elif(tdvd=='duplo'):
                valorC=tcomum*2
            else:
                print('Não temos essa opção!')
    elif(quantfilme>1):
        while(quantfilme>=1):
            tfilme=str.lower(input('O tipo de filme é lançamento ou comum? '))
            tdvd=str.lower(input('O tipo de dvd é simples ou duplo? '))
            quantfilme-=1
            if(tfilme=='lançamento'):
                if(tdvd=='simples'):
                    valorL+=tlanc
                elif(tdvd=='duplo'):
                    valorL+=tlanc*2
                else:
                    print('Não temos essa opção!')
            elif(tfilme=='comum'):
                if(tdvd=='simples'):
                    valorC+=tcomum
                elif(tdvd=='duplo'):
                    valorC+=tcomum*2
                else:
                    print('Não temos essa opção!')
            else:
                print('Não temos essa opção!')
    else:
        print('\n',valorL,'R$ de filme(s) de lançamento')
        print('\n',valorC,'R$ de filme(s) comum')
        print(' Totalizando',valorL+valorC-((valorL+valorC)*desconto),'R$ do(s) filme(s)')
        print(' Com um desconto de',(valorL+valorC)*desconto)
elif(cliente=='especial'):
    if(quantfilme==1):
        tfilme=str.lower(input('O tipo de filme é lançamento ou comum? '))
        tdvd=str.lower(input('O tipo de dvd é simples ou duplo? '))
        if(tfilme=='lançamento'):
            if(tdvd=='simples'):
                valorL=tlanc
            elif(tdvd=='duplo'):
                valorL=tlanc*2
            else:
                print('Não temos essa opção!')
        elif(tfilme=='comum'):
            if(tdvd=='simples'):
                valorC=tcomum
            elif(tdvd=='duplo'):
                valorC=tcomum*2
            else:
                print('Não temos essa opção!')
    elif(quantfilme>1):
        while(quantfilme>=1):
            tfilme=str.lower(input('O tipo de filme é lançamento ou comum? '))
            tdvd=str.lower(input('O tipo de dvd é simples ou duplo? '))
            quantfilme-=1
            if(tfilme=='lançamento'):
                if(tdvd=='simples'):
                    valorL+=tlanc
                elif(tdvd=='duplo'):
                    valorL+=tlanc*2
                else:
                    print('Não temos essa opção!')
            elif(tfilme=='comum'):
                if(tdvd=='simples'):
                    valorC+=tcomum
                elif(tdvd=='duplo'):
                    valorC+=tcomum*2
                else:
                    print('Não temos essa opção!')
            else:
                print('Não temos essa opção!')
    else:
        print('\n',valorL,'R$ de filme(s) de lançamento')
        print('\n',valorC,'R$ de filme(s) comum')
        print(' Totalizando',valorL+valorC-((valorL+valorC)*desconto),'R$ do(s) filme(s)')
        print(' Com um desconto de',(valorL+valorC)*desconto,'R$')
