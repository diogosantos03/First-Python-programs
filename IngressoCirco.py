while(True):
    setor=str.lower(input('setor: '))
    ingresso=str.lower(input('ingresso: '))
    if(setor=='arquibancada'):
        if(ingresso=='inteira'):
            valor=((5/100)*100)+100
            print('R$',valor)
        elif(ingresso=='meia'):
            valor=(((5/100)*100)+100)/2
            print('R$',valor)
        else:
            print('Tipo de ingresso inválido')
    elif(setor=='cadeira'):
        if(ingresso=='inteira'):
            valor=(5/100)*200+200
            print('R$',valor)
        elif(ingresso=='meia'):
            valor=(((5/100)*200)+200)/2
            print('R$',valor)
        else:
            print('Tipo de ingresso inválido')
    elif(setor=='platéia vip'):
        if(ingresso=='inteira'):
            valor=(5/100)*350+350
            print('R$',valor)
        else:
            print('Tipo de ingresso inválido')
    else:
        print('setor inválido')
