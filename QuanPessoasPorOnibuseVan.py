while(True):
    quantpessoas=float(input('Quantas pessoas vão viajar? '))
    PrecoVan=200
    PrecoOnibus=350
    if(quantpessoas<=0):
        print('Número de pessoas inválido')
    else:
        if(quantpessoas>0)and(quantpessoas<=20):
            valor=PrecoVan/quantpessoas
            print('1 Vam e aproximadamente',valor,'R$ por pessoa')
        elif(quantpessoas>20)and(quantpessoas<=40):
            valor=2*(PrecoVan/quantpessoas)
            print('2 Vans e aproximadamente',valor,'R$ por pessoa')
        elif(quantpessoas>40)and(quantpessoas<42):
            valor=PrecoVan/quantpessoas
            print('3 Vans e aproximadamente',valor,'R$ por pessoa')
        else:
            vagas=quantpessoas//42
            print(vagas,'Ônibus')
            vagas1=quantpessoas%42
            if(vagas1>0)and(vagas1<=20):
                valor=(PrecoVan+PrecoOnibus)/quantpessoas
                print('1 Van e aproximadamente',valor,'R$ por pessoay')
            elif(vagas1>20)and(vagas1<=40):
                valor=(PrecoVan+PrecoVan+PrecoOnibus)/quantpessoas
                print('2 Vans e aproximadamente',valor,'R$ por pessoaw')
            elif(vagas1>40)and(vagas1<42):
                valor=(PrecoVan+PrecoVan+PrecoVan+PrecoOnibus)/quantpessoas
                print('3 Vans e aproximadamente',valor,'R$ por pessoaaa')
