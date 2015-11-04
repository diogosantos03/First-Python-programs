tlanc=4
tcomum=3
valor=0
tfilme=str.lower(input('O tipo de filme é lançamento ou comum? '))
tdvd=str.lower(input('O tipo de dvd é simples ou duplo? '))
if(tfilme=='lançamento'):
    if(tdvd=='simples'):
        valor=tlanc
    elif(tdvd=='duplo'):
        valor=tlanc*2
    else:
        print('Não temos essa opção!')
elif(tfilme=='comum'):
    if(tdvd=='simples'):
        valor=tcomum
    elif(tdvd=='duplo'):
        valor=tcomum*2
    else:
        print('Não temos essa opção!')
else:
    print('Não temos essa opção!')
print(valor,'R$')
