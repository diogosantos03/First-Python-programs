altura = float (input('qual sua altura: '))
while(altura!=000):
    if (altura <= 1.40):
        print('Estatura Baixa')
    else:
        if (altura < 1.65):
            print('Estatura Mediana')
        else:
            print('Estatura Alta')
    altura = float (input('qual sua altura: '))
print('vc saiu!')
