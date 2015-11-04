cont=1000
palavra=''
letras=str.lower(input('Informe uma letra: '))
while(letras!=''):
    palavra+=letras
    letras=str.lower(input('Informe uma letra: '))
print(palavra)
