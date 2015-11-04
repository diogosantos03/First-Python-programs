while(True):
    salario=float(input('informe seu salário: '))
    vint=(20/100)*salario
    quin=(15/100)*salario
    dez=(10/100)*salario
    cin=(5/100)*salario
    if(salario<=0):
        print('salário inválido!')
    else:
        if(salario>0)and(salario<280):
            ajus=vint+salario
            print('seu salário de',salario,'teve um aumento de 20%, que equivale a',vint,', somando dá',ajus)
        elif(salario>=280)and(salario<700):
            ajus=quin+salario
            print('seu salário de',salario,'teve um aumento de 15%, que equivale a',quin,', somando dá',ajus)
        elif(salario>=700)and(salario<1500):
            ajus=dez+salario
            print('seu salário de',salario,'teve um aumento de 10%, que equivale a',dez,', somando dá',ajus)
        elif(salario>1500):
            ajus=cin+salario
            print('seu salário de',salario,'teve um aumento de 5%, que equivale a',cin,', somando dá',ajus)
