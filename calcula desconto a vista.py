while(True):
    valorproduto=float(input('Informe um valor: '))
    formapagamento=str.lower(input('Qual a forma de pagamento? '))
    desconto=10
    valor=0
    din='dinheiro'
    che='cheque'
    if(valorproduto>=100):
        if(formapagamento==din):
            valor=(desconto/100)*valorproduto
            print('Vc vai pagar',valorproduto-valor,'R$ e teve um desconto de 10% que equivale a',valorproduto%(valorproduto-valor),'R$')
        elif(formapagamento==che):
            valor=valorproduto
            print(valor)
        else:
            print('Forma de pagamento inválida!!!')
    elif(valorproduto<100):
        if(formapagamento==din):
            valor=valorproduto
            print('Vai pagar',valor,'vc só terá descontos nas compras a dinheiro e igual ou maior que 100R$')
        elif(formapagamento==che):
            valor=valorproduto
            print('Vai pagar',valor,'R$ e só terá descontos nas compras a dinheiro e igual ou maior que 100R$')
        else:
            print('Forma de pagamento inválida')
