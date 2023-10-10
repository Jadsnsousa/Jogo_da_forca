# importando bibliotecas.
from random import randint
from time import sleep

"""
Jogo da forca desenvolvido por: Jadson Sousa
Linkedin: https://www.linkedin.com/in/devjadsnsousa/

Durante o curso avançado de python, foi solicitado que o estudante desenvolva um jogo da forca.
Está é a minha solução para o exercicio do jogo da forca.

"""

# definindo as palavras que serão jogadas.
PALAVRAS = ('casa', 'professor', 'desenvolvedor', 'estudante', 'queijo', 'mel', 'mapa',
            'amigos', 'gratidao', 'carro', 'motorista', 'elefante', 'computador')

fim = True

# Iniciando o jogo da forca.
print(f'INICIANDO JOGO DA FORCA')
sleep(2)
print(f'PREENCHENDO O SISTEMA...')
sleep(2)

while fim:
    
    # Menu de opções:
    print(f'MENU DE OPÇÕES'\
        f'\n[1] Jogar'\
        f'\n[2] Fechar')
    MENU = str(input('ESCOLHA: '))[0]
    while MENU not in '12':
        MENU = str(input('OPÇÃO INVALIDA. ESCOLHA: '))[0]
        
    if MENU == '1':
        print(f'\nSORTEANDO PALAVRAS...')
        sleep(1)
        
        palavra_final = list()  # Variavel para verificar se a palavra final é a correta.
        chutes = list() # Criando uma lista para armazenar as letras que foi digitada pelo usuário.
          
        # Escolhendo a palavra utilizando a função randint da biblioteca random.
        palavra_aleatoria = PALAVRAS[randint(0, len(PALAVRAS) - 1)]
        
        palavra_secreta = list()    # Criando uma lista para mostrar os caracteres da frase.
        erros = 5   # Definindo a quantidade de chances que o jogador tem.
    
        # Aprendendo as "-" de acordo com o tamanho da palavra escolhida.
        for c in range(0, len(palavra_aleatoria)):
            palavra_secreta.append('-')
        
        # Criei a variavel PALAVRA_FINAL para verificar se o usuário ganhou ou perdeu.
        for L in palavra_aleatoria:
            palavra_final.append(L)
            
        print(f'\nA palavra escolhida possui: {len(palavra_secreta)} letras.')
        sleep(2)
        
        # While para rodar enquanto o numero de tentativas for maior que 0.
        while True:
            print(f'Tentativas restantes: {erros}')
            sleep(1.5)
            letra = str(input('\nDigite um letra ou digite "CHUTE" para digitar a palavra: ')).lower()
            chutes.append(letra)
            print(f'Você já digitou as seguintes letras: {chutes}')
            sleep(1.5)

            
            # Se o usuário souber a palavra, basta ele digitar "CHUTE".
            # Durante o chute, se o usuário chutar uma palavra errada, ele perde o jogo.
            # Se a palavra for correta, ele ganha o jogo.
            if letra == 'chute':
                palavra_chute = str(input(f'Digite a palavra:'))
                if palavra_chute == palavra_aleatoria:
                    palavra_secreta.clear()
                    break
                else:
                    print(f'Você errou, a palavra secreta é: {palavra_aleatoria}')
                    sleep(2)
                    break
                    
            # Se a letra digitada estiver na palavra_aleatoria, é substituido o '-' pela letra.        
            elif letra in palavra_aleatoria:
                for c in range(0, len(palavra_aleatoria)):
                    if letra == palavra_aleatoria[c]:
                        palavra_secreta[c] = letra
                print(f'Você acertou, a letra [{letra}] aparece na palavra.')
                sleep(2)
            else:
                erros -= 1
                print(f'a letra [{letra}] não aparece na palavra. Tente novamente...')
                sleep(2)
            
            print(f'Palavra secreta: {palavra_secreta}')

            if erros == 0 or '-' not in palavra_secreta:
                break
            # Verificando se o jogador ganhou ou perdeu.      
        if palavra_secreta == palavra_final or palavra_chute == palavra_aleatoria:
            print(f'\nVocê ganhou!!'\
                f'\nA palavra secreta é: {palavra_aleatoria}\n')
            sleep(5)
            chutes.clear()
            palavra_secreta.clear()
            
        else:
            print(f'Você perdeu... Tente novamente.\n')
            sleep(5)
            chutes.clear()
            palavra_secreta.clear()

    elif MENU == '2':
        print(f'FINALIZANDO JOGO...')
        sleep(2)
        break
    
    print(f'Reiniciando o jogo...\n')
    sleep(2)
else:
    print(f'JOGO FINALIZADO COM SUCESSO.')
            