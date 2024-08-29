import random 
#aqui temos uma função que pega o total de pedra, papel e tesoura, e faz uma média de quanto cada um apareceu, depois ela retorna a probabilidade de cada um acontecer
def probabilityJokenpo(pedra, papel, tesoura):
    total = pedra + papel + tesoura
    sorteio = random.randint(1, total)
    if sorteio <= pedra:
        return counterDoLance(0)
    elif sorteio > pedra and sorteio <= (pedra + papel):
        return counterDoLance(1)
    else: 
        return counterDoLance(2)

#aqui temos uma função que entrega o lance vitórioso contra um lance previsto
#0 é pedra, 1 é papel, 2 é tesoura
def counterDoLance(lance = int):
    if lance == 0:
        return 1
    elif lance == 1:
        return 2
    return 0

#essa função calcula o resultado de um turno
#0 é pedra, 1 é papel, 2 é tesoura
def jokenpoResult(lance1 = int, lance2 = int):

    if lance1 == 0 and lance2 == 2:
        print('Você ganhou! Pedra ganha de tesoura')
        return 'victory'
    elif lance1 == 0 and lance2 == 1:
        print('Você perdeu! Pedra perde para papel')
        return 'defeat'
    elif lance1 == 1 and lance2 == 0:
        print('Você ganhou! Papel ganha da pedra')
        return 'victory'
    elif lance1 == 1 and lance2 == 2:
        print('Você perdeu! Papel perde para tesoura')
        return 'defeat'
    elif lance1 == 2 and lance2 == 1:
        print('Você ganhou! Tesoura ganha de papel')
        return 'victory'
    elif lance1 == 2 and lance2 == 0:
        print('Você perdeu! Tesoura perde para pedra')
        return 'defeat'
    elif lance1 == lance2:
        print('empate')
        return 'draw'
    return False

def jokenpoConverter(lance=int):
    if lance == 'pedra':
        return 0
    elif lance == 'papel':
        return 1
    elif lance == 'tesoura':
        return 2
    elif lance == 0:
        return 'pedra'
    elif lance == 1:
        return 'papel'
    elif lance == 2:
        return 'tesoura'
    
    return False    

            
