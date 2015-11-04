while(True):
    combustivel=str.lower(input('Qual bombustivel: '))
    dinh=float(input('Qual valor: '))
    if(combustivel=='gasolina'):
        valor=dinh/2.53
        print('vc abasteceu','%.2f'%valor,'litros e não ganhou a troca de óleo')
    elif(combustivel=='diesel'):
        valor=dinh/1.92
        print('vc abasteceu','%.2f'%valor,'litros e não ganhou a troca de óleo')
    elif(combustivel=='etanol'):
        valor=dinh/2.09
        if(valor>30):
            print('vc abasteceu','%.2f'%valor,' e ganhou uma troca de óleo')
        else:
            print('vc abasteceu','%.2f'%valor,'litros e não ganhou a troca de óleo')
    else:
        print('Combustível inválido')
