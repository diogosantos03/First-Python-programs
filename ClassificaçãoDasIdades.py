idade=int(input('Informe sua idade: '))
quantjovens=0
quantadultos=0
media=0
soma=0
mdade=0
while(idade>0):
    if(idade<=20):
        quantjovens+=1
    elif(idade>20)and(idade<60):
        if(idade>mdade):
            mdade=idade
    else:
        quantadultos+=1
        soma+=idade
        media=soma/quantadultos
    idade=int(input('Informe sua idade: '))
if(quantjovens==0)or(quantadultos==0)or(media==0):
    if(quantjovens==0):
        print('Não há jovens!')
        if(mdade>0):
            print(mdade,'é a maior idade de um adulto')
        else:
            print('Não há adultos')
        if(media>0):
            print(media,'é a média de idade dos idosos')
        else:
            print('Não há idosos!')
    else:
        print(quantjovens,'é a quantidade de jovens')
        print(mdade,'é a maior idade de um adulto')
        print(media,'é a média de idade dos idosos')















if(quantjovens==0)or(quantadultos==0)or(media==0):
    if(quantjovens==0):
        print('ñ ha jovens!')
