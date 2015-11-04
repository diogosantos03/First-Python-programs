num=int(input('Informe um número: '))
maior=0
while(num>=0):
    if(num>maior):
        maior=num
    num=int(input('Informe um número: '))
print('O maior número foi:',maior)
