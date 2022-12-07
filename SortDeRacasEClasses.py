import random

def menu():
    print('\n***********************************')
    print('*  Bem vindo ao Menu!             *')
    print('* 1 - Escolha de Raça             *')
    print('* 2 - Escolha de Classe           *')
    print('* 0 - Sair                        *')
    print('***********************************')

def escolheRaca():

    racas = {1:'Humano',
             2:'Anão',
             3:'Dahllan',
             4:'Elfo',
             5:'Goblin',
             6:'Lefou',
             7:'Minotauro',
             8:'Qareen',
             9:'Golem',
             10:'Hynne',
             11:'Kliren',
             12:'Medusa',
             13:'Osteon',
             14:'Sereia/Tritão',
             15:'Sílfide',
             16:'Suraggel',
             17:'Trog'}

    raca = random.randint(1, 17)
    racaescolhida = racas[raca]

    print('Raça Sorteada: {}'.format(racas[raca]))

    return racaescolhida

def escolheClasse():
    classes = {1: 'Arcanista',
               2: 'Bárbaro',
               3: 'Bardo',
               4: 'Bucaneiro',
               5: 'Caçador',
               6: 'Caçador',
               7: 'Cavaleiro',
               8: 'Clérigo',
               9: 'Druida',
               10: 'Guerreiro',
               11: 'Inventor',
               12: 'Ladino',
               13: 'Lutador',
               14: 'Nobre',
               15: 'Paladino'}

    classe = random.randint(1, 15)

    print('Raça Sorteada: {}'.format(classes[classe]))

menu()

'''saida = []
jogador = input('Digite o nome do Jogador: ')
saida.append(jogador)'''

escolha = int(input('\nDigite a opção desejada: \n'))

while escolha != 0:
    if escolha == 1:
        escolheRaca()
        input('\nPressione qualquer tecla para continuar...')
    elif escolha == 2:
        escolheClasse()
        input('\nPressione qualquer tecla para continuar...')

    menu()
    escolha = int(input('\nDigite a opção desejada: \n'))