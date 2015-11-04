cont=5
while(cont>=1):
    rendaAnual = float (input('quanto vc ganha: '))
    cont-=1
    if (rendaAnual <= 12000):
        imposto = 0
    if (rendaAnual > 60000):
        imposto = rendaAnual*0.07
    else:
        imposto = rendaAnual*0.0
    print(imposto)
