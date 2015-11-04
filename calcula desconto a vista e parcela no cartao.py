while(True):
    valorproduto=int(input('Informe o valor da compra: '))
    formapagamento=str.lower(input('Vc vai pagar a dinheiro, cheque ou cartão? '))
    desconto=10
    valor=0
    din='dinheiro'
    che='cheque'
    car='cartão'
    deb='débito'
    cre='crédito'
    if(valorproduto>=100):
        if(formapagamento==din):
            valor=(desconto/100)*valorproduto
            print('Vc vai pagar',valorproduto-valor,'R$ e teve um desconto de 10% que equivale a',valorproduto%(desconto/100)*valorproduto,'R$')
            print(80*'*')
        elif(formapagamento==che):
            valor=valorproduto
            print('Vai pagar',valor,'R$ e só terá descontos nas compras a dinheiro maior ou igual a 100R$')
            print(80*'*')
        elif(formapagamento==car):
            print(80*'*')
            print('VC VAI PAGAR NO CARTÃO DE DÉBITO OU CRÉDITO?')
            forma=str.lower(input('Informe a forma de pagamento no cartão: '))
            if(forma==deb):
                print('Vai pagar',valorproduto,'R$ e só terá descontos nas compras a dinheiro maior ou igual a 100R$')
                print(80*'*')
            elif(forma==cre):
                print('Vc pode pagar',valorproduto,'R$ em até 3 parcelas')
                parcelas=int(input('Deseja pagar em quantas parcelas? '))
                if(parcelas<1)or(parcelas>3):
                    print('Número de parcelas inválidas!!!')
                    print(80*'*')
                else:
                    print('Vc vai pagar',valorproduto,'em',parcelas,'parcelas de',valorproduto/parcelas)
                    print(80*'*')
            else:
                print('Forma de pagamento inválida!!!')
                print(80*'*')
        else:
            print('Forma de pagamento inválida!!!')
            print(80*'*')
    elif(valorproduto<100):
        if(formapagamento==din):
            valor=valorproduto
            print('Vai pagar',valor,'R$, vc só terá descontos nas compras a dinheiro maior ou igual a 100R$')
            print(80*'*')
        elif(formapagamento==che):
            valor=valorproduto
            print('Vai pagar',valor,'R$ e só terá descontos nas compras a dinheiro maior ou igual a 100R$')
            print(80*'*')
        elif(formapagamento==car):
            print(80*'*')
            print('VC VAI PAGAR NO CARTÃO DE DÉBITO OU CRÉDITO?')
            forma=str.lower(input('Informe a forma de pagamento no cartão: '))
            if(forma==deb):
                print('Vai pagar',valorproduto,'R$ e só terá descontos nas compras a dinheiro maior ou igual a 100R$')
                print(80*'*')
            elif(forma==cre):
                print('Vc pode pagar',valorproduto,'R$ em até 3 parcelas.')
                parcelas=int(input('Deseja pagar em quantas parcelas? '))
                if(parcelas<1)or(parcelas>3):
                    print('Número de parcelas inválidas!!!')
                    print(80*'*')
                else:
                    print('Vc vai pagar',valorproduto,'R$ em',parcelas,'parcelas de',valorproduto/parcelas,'R$')
                    print(80*'*')
        else:
            print('Forma de pagamento inválida')
            print(80*'*')
