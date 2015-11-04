#Sorteia os times e os resultados de cada jogo e diz quem ganhou e empatou!!!
import random
Qjogos=20
Qtimes=77
QMáximaGols=4
usuario=str.lower(input('Qual seu time de coração:'))
times=['abc/rn','américa/mg','américa/rn','américa/rj','atlético/go','atlético/mg','atlético/pr','avaí/sc','bahia/ba','bangú/rj','barueri/sp','botafogo/pb','botafogo/rj','bragantino/sp','brasiliense/df','ceará/ce','corinthians/sp','coritiba/pr','crb/al','criciúma/sc','cruzeiro/mg','csa/al','desportiva/es','figueirense/sc','flamengo/rj','fluminense/rj','fortaleza/ce','gama/df','góias/go','grêmio/rs','guaraní/sp','inter limeira/sp','internacional/rs','ipatinga/mg','ituano/sp','ji-paraná/ro','joinville/sc','juventus/sp','londrina/pr','marília/sp','mixto/mt','moto clube/ma','nácional/am','náutico/pe','olaria/rj','operários/ms','palmas/to','palmeiras/sp','paraná/pr','paulista/sp','paysandú/pa','ponte preta/sp','port desport/sp','reno/pa','rio branco/ac','rio branco/es','river/pi','roraima/rr','sampaio corrêia/ma','santa cruz/pe','santo andré/sp','santos/sp','são caetano/sp','são paulo/sp','são raimundo/am','sergipe/se','sport/pe','treze/pb','tuna luso/pa','uberlândia/mg','união barbarense/sp','união são joão/sp','vasco/rj','vila nova/go','villa nova/mg','vitória/ba','xv piracicaba/sp','ypiranga/ap']
#Times=['ABC/RN','América/MG','América/RN','América/RJ','Atlético/GO','Atlético/MG','Atlético/PR','Avaí/SC','Bahia/BA','Bangú/RJ','Barueri/SP','Botafogo/PB','Botafogo/RJ','Bragantino/SP','Brasiliense/DF','Ceará/CE','Corinthians/SP','Coritiba/PR','CRB/AL','Criciúma/SC','Cruzeiro/MG','CSA/AL','Desportiva/ES','Figueirense/SC','Flamengo/RJ','Fluminense/RJ','Fortaleza/CE','Gama/DF','Góias/GO','Grêmio/RS','Guaraní/SP','Inter Limeira/SP','Internacional/RS','Ipatinga/MG','Ituano/SP','Ji-paraná/RO','Joinville/SC','Juventus/SP','Londrina/PR','Marília/SP','Mixto/MT','Moto Clube/MA','Nácional/AM','náutico/PE','Olaria/RJ','Operários/MS','Palmas/TO','Palmeiras/SP','Paraná/PR','Paulista/SP','Paysandú/PA','Ponte Preta/SP','Port Desport/SP','Reno/PA','Rio Branco/AC','Rio Branco/ES','River/PI','Roraima/RR','Sampaio Corrêia/MA','Santa Cruz/PE','Santo André/SP','Santos/SP','São Caetano/SP','São Paulo/SP','São Raimundo/AM','Sergipe/SE','Sport/PE','Treze/PB','Tuna Luso/PA','Uberlândia/MG','União Barbarense/SP','União São João/SP','Vasco/RJ','Vila Nova/GO','Villa Nova/MG','Vitória/BA','XV Piracicaba/SP','Ypiranga/AP']
for rodada in range(0,Qjogos):
    for t in range(0,2):
        time1=random.randint(0,Qtimes)
        time2=random.randint(0,Qtimes)
    for gols in range(0,2):
        sorteio3=random.randint(0,QMáximaGols)
        sorteio4=random.randint(0,QMáximaGols)
    if(sorteio3>sorteio4):
        print(times[time1],sorteio3,'   É o vencedor')
        print(times[time2],sorteio4,'\n',12*'-')
    elif(sorteio4>sorteio3):
        print(times[time1],sorteio3)
        print(times[time2],sorteio4,'   É o vencedor','\n',12*'-')
    else:
        print(times[time1],sorteio3,'   Empatou')
        print(times[time2],sorteio4,'   Empatou','\n',12*'-')
if(times.count(usuario)==0):
    print('Não existe esse time!')
else:
    print('Sim, temos esse time!')
