from random import randint
import jokenpoFunctions as jf
import csv

#aqui guardamos o historico de jogos
plays = []

# uma variavel que guarda a quantidade de vezes que pedra foram jogadas
pedra = 0

# uma variavel que guarda a quantidade de vezes que papel foram jogadas
papel = 0

# uma variavel que guarda a quantidade de vezes que tesoura foram jogadas
tesoura = 0


#jokenpo é o historico inteiro das jogadas da MAQUINA em 1 rodada
jokenpo = []

#essa condição foi criada para que no primeiro jokenpo, se o empate acontecer, ele identificar que precisa 
#escrever o head do banco de dados
first_turn = 0

#aqui escrevemos o head do nosso csv
with open('jokenpo.csv', 'w', newline='') as csvfile:
        campos_head=['historico_do_usuario', 'vitorias_do_usuario']
        writer = csv.DictWriter(csvfile, fieldnames=campos_head)
        writer.writeheader()





print('Bem vindo ao Jokenpo')
lance = input('Digite pedra, papel ou tesoura. Ou digite 3 para encerrar o jogo ')
#Aqui nós adicionamos o lance a variavel respectiva
if jf.jokenpoConverter(lance) == 0:
        pedra += 1
elif jf.jokenpoConverter(lance) == 1:
    papel += 1
else:
    tesoura += 1


#aqui nos definimos lances aleatorios até termos uma base de dados boa
if papel + pedra + tesoura < 5:
    lance_maquina = randint(0, 2)

    
else:
#aqui nos analisamos os lances do turno respectivo dos jogos anteriores, e pegamos o com maior probabilidade de 
#vitoria
    lance_mais_provavel = jf.probabilityJokenpo(pedra, papel, tesoura)
    lance_maquina = lance_mais_provavel

#não precisava da linha 54, so fiz para melhorar a compreensão

#aqui nos processamos o resultado e colocamos a saída na variável 'res'
print(f'A maquina joga: {jf.jokenpoConverter(lance_maquina)}')
res = jf.jokenpoResult(jf.jokenpoConverter(lance), lance_maquina)

#aqui nos processamos o resultado para definir como o programa irá proceder
if res == 'victory':
    plays.append(lance)
    with open('jokenpo.csv', 'a+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=campos_head)
        writer.writerow({'historico_do_usuario':plays, 'vitorias_do_usuario': 1})
    plays = []

elif res == 'defeat':
    plays.append(lance)
    with open('jokenpo.csv', 'a+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=campos_head)
        writer.writerow({'historico_do_usuario': plays, 'vitorias_do_usuario': 1})
    plays = []
elif res == 'draw':
    plays.append(lance)
    

while lance != 3:
    lance = input('Digite pedra, papel ou tesoura. Ou digite 3 para encerrar o jogo ')
    if jf.jokenpoConverter(lance) == 0:
        pedra += 1
    elif jf.jokenpoConverter(lance) == 1:
        papel += 1
    else:
        tesoura += 1
    if papel + pedra + tesoura < 5:
        lance_maquina = randint(0, 2)
        
    else:
        lance_mais_provavel = jf.probabilityJokenpo(pedra, papel, tesoura)
        lance_maquina = lance_mais_provavel
    print(f'A maquina joga: {jf.jokenpoConverter(lance_maquina)}')
    res = jf.jokenpoResult(jf.jokenpoConverter(lance), lance_maquina)

    if res == 'victory':
        plays.append(lance)
        with open('jokenpo.csv', 'a+', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=campos_head)
            writer.writerow({'historico_do_usuario':plays, 'vitorias_do_usuario': 1})
        plays = []

    elif res == 'defeat':
        plays.append(lance)
        with open('jokenpo.csv', 'a+', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=campos_head)
            writer.writerow({'historico_do_usuario':plays, 'vitorias_do_usuario': 0})
        plays = []
    elif res == 'draw':
        plays.append(lance)


