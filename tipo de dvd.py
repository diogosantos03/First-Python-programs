tfilme=str.lower(input('Lançamento ou comum? '))
tdvd=str.lower(input('simples ou duplo? '))
lanc=4
simpl=3
if(tfilme=='lançamento'):
    if(tdvd=='simples'):
        print(lanc)
    elif(tdvd=='duplo'):
        print(lanc*2)
    else:
        print('não temos essa opção!')
elif(tfilme=='comum'):
    if(tdvd=='simples'):
        print(simpl)
    elif(tdvd=='duplo'):
        print(simpl*2)
    else:
        print('não temos essa opção!')
else:
    print('não temos essa opção!')
