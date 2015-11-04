while(True):
    nota1=float(input('primeira nota: '))
    nota2=float(input('segunda nota: '))
    media=nota1+nota2/2
    if(media<0):
        print('reprovadissimo com',media)
    elif(media>0)and(media<7):
        print('reprovado com',media)
    elif(media>=7)and(media<10):
        print('aprovado com',media)
    else:
        print('aprovado com média 10, parabéns!')
