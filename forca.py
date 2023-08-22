# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from functools import reduce

# Board (tabuleiro)

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        print('>' * 10, 'Hangman', '<' * 10)
        self.vidas = 6
        self.resposta = word
        self.LBoard = list('_' * len(word))
        self.LErr = []
        self.LCor = []
        self.boneco = board

    # Método para adivinhar a letra
    def guess(self, letter):
        # se tiver na palavra
        aux = True
        if self.resposta.count(letter) != 0:  # se  há a letra na palavra
            self.LCor.append(letter)  # adiciona na lista de corretas
            print('Acertou miserávi')
        else:  # se não achou letra
            self.LErr.append(letter)  # adiciona na lista de erradas
            self.vidas -= 1  # reduz a vida
            print('Tente novamente')

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.vidas == -1:
            return True

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        X = list(filter(lambda l: l != '_', self.LBoard))
        if len(X) == len(self.resposta):
            return True

    # Método para não mostrar a letra no board
    def hide_word(self):
        if len(self.LCor) != 0:
            saida = []
            for x in self.resposta:  # passa toda palavra
                aux = True
                for y in self.LCor:  # percorre o vetor de palavras encontradas
                    if x == y:  # se encontra uma letra já encontrada adiciona a saida
                        aux = False
                        saida.append(x)
                if aux:  # se nao achou nenhuma letra, adiciona tracinho
                    saida.append('_')
            self.LBoard = saida

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(self.boneco[6 - self.vidas])  # Mostra o boneco

        print('Palavra: ', reduce(lambda x, y: x + ' ' + y, self.LBoard))  # Mostra as palavras já descobertas

        # Mostra as tentativas
        print('Letras erradas:')
        if len(self.LErr) != 0:
            print(reduce(lambda x, y: x + ' - ' + y, self.LErr))
        print('Letras corretas:')
        if len(self.LCor) != 0:
            print(reduce(lambda x, y: x + ' - ' + y, self.LCor))


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not (game.hangman_over()) and not (game.hangman_won()):
        # Verifica o status do jogo
        game.print_game_status()
        while True:
            letra = str(input('Digite uma letra: ')).strip()
            letra = letra.upper()
            if game.LCor.count(letra) != 0 or game.LErr.count(letra) != 0:
                print('Letra já foi escolhida antes!!')
            elif letra == '\n' or letra == '':
                continue
            else:
                break
        game.guess(letra)
        game.hide_word()  # atualiza letras já encontradas
    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!  ""%s""' %game.resposta)
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.resposta)

    print('\nBom jogo !!\n')


# Executa o programa
if __name__ == "__main__":
    main()
