num=int(input('Informe um número: '))
while(num<=5):
    print('digite um número maior que cinco!')
    num=int(input('Informe um número: '))
else:
    for diogo in range(1,num+1):
        if(diogo%3==0):
            print('#',diogo,'É multiplo de três.\n')
        if(diogo%2==0):
            print('#',diogo,'É número par.\n')
        if(diogo**2==diogo*diogo):
            print('# A raiz quadrada de',diogo*diogo,'é <',diogo,'>\n')
            print('---------------------------------')

