nome=input('Cadastre seu nome: ')
senha=int(input('Cadastre uma senha: '))
n=nome
s=senha
print('Cadastro efetuado seu nome e senha é',n,s)
print('agora vc pode entrar no sistema!')
nomee=input('digite seu nome: ')
senhaa=int(input('digite sua senha: '))
while(n==nomee)and(s==senhaa):
    print('login efetuado com sucesso')
    nomee=input('digite seu nome: ')
    senhaa=int(input('digite sua senha: '))
print('nome ou senha inválida!')
