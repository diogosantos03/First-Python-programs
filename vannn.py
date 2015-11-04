#O while(true) é apenas p/ fazer o testes mais rápidos.
while(True):
    quantpessoas=float(input('Quantas pessoas vão viajar? '))
    PrecoVan=200
    PrecoOnibus=350
    if(quantpessoas<=0):
        print('Número de pessoas inválido')
    else:
        if(quantpessoas>0)and(quantpessoas<=20):
            valor=PrecoVan/quantpessoas
            print('1 Vam   (primeiro print)')
        elif(quantpessoas>20)and(quantpessoas<=40):
            valor=2*(PrecoVan/quantpessoas)
            print('2 Vans   (segundo print)')
        else:
            QuantOnibus=quantpessoas//42
            print(QuantOnibus,'Ônibus')
            QuantVans=quantpessoas%42
            if(QuantOnibus>0)and(QuantOnibus==1):
                if(QuantVans>0)and(QuantVans<=20):
                    valor=(PrecoVan+PrecoOnibus)/quantpessoas
                    print('1 Van    quarto print)')
                elif(QuantVans>20)and(QuantVans<=40):
                    valor=(PrecoVan+PrecoVan+PrecoOnibus)/quantpessoas
                    print('2 Vans    quinto print)')
                elif(QuantVans>40)and(QuantVans<42):
                    valor=(PrecoVan+PrecoVan+PrecoVan+PrecoOnibus)/quantpessoas
                    print('3 Vans    sexto print)')
#e o pq que ñ entra no 'nono print' abaixo???
            elif(QuantOnibus>1):
                NovoPrecoOnibus=PrecoOnibus*QuantOnibus
                if(QuantVans>0)and(QuantVans<=20):
                    valor=(PrecoVan+NovoPrecoOnibus)/quantpessoas
                    print('1 Van    sétimo print)')
                elif(QuantVans>20)and(QuantVans<=40):
                    valor=((PrecoVan*2)+NovoPrecoOnibus)/quantpessoas
                    print('2 Vans    oitavo print)')
                elif(QuantVans>40)and(QuantVans<42):
                    valor=((PrecoVan*3)+NovoPrecoOnibus)/quantpessoas
                    print('3 Vans    nono print)')
        print('Aproximadamente','%.2f' % valor,'R$ por pessoa')
                
                
