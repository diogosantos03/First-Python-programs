while(True):
    precoA=float(input('informe um número: '))
    precoB=float(input('informe um número: '))
    precoC=float(input('informe um número: '))
    if(precoA<precoB)and(precoA<precoC):
        menor=precoA
    elif(precoB<precoA)and(precoB<precoC):
        menor=precoB
    else:
        menor=precoC
    print('vc deve comprar o produto de menor preço, que é',menor)
