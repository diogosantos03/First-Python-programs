quantfilme=int(input('Vai alugar quantos filmes? '))
tlanc=4
tcomum=3
valorC=0
valorL=0
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
if(quantfilme<=0):
    print('Vc digitou: 0 ou número negativo ou forneceu informações erradas!')
else:
    print(valorL,'R$ de filme(s) de lançamento')
    print(valorC,'R$ de filme(s) comum')
    print('Totalizando',valorL+valorC,'R$ do(s) filme(s)')
