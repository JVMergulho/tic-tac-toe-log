# Jogo da velha - 03/08/22
# João Vitor Mergulhão

# Imprime o tabuleiro atualizado
def tabuleiro(casas):
    print('\n')
    print('    1   2   3')
    print(f'1   {casas[0][0]} | {casas[0][1]} | {casas[0][2]} ')
    print('  -------------')
    print(f'2   {casas[1][0]} | {casas[1][1]} | {casas[1][2]} ')
    print('  -------------')
    print(f'3   {casas[2][0]} | {casas[2][1]} | {casas[2][2]} ')


# Recebe o índice da casa e insere o elemento
def jogar(cont, casas):
    # 'X' joga primeiro e 'O' depois
    if cont % 2 == 0:
        simbolo = 'X'
    else:
        simbolo = 'O'

    index = [-1, -1]

    while index[0] < 0 or index[0] > 2 or index[1] < 0 or index[1] > 2:
        index = input('\nEm qual casa deseja jogar?\n')
        index = index.split('/')
        index[0] = int(index[0]) - 1
        index[1] = int(index[1]) - 1
        if casas[index[0]][index[1]] != ' ':
            index = [-1, -1]

    casas[index[0]][index[1]] = simbolo


# Checa se alguém venceu
def vitoria(casas):
    check = False

    # Caso horizontal
    for i in range(0, 3):
        if casas[i][0] == casas[i][1] and casas[i][1] == casas[i][2]:
            check = True

    # Caso vertical
    for i in range(0, 3):
        if casas[0][i] == casas[1][i] and casas[1][i] == casas[2][i]:
            check = True

    # Casos diagonais
    if casas[0][2] != ' ':
        if casas[0][2] == casas[1][1] and casas[1][1] == casas[2][0]:
            check = True

    if casas[0][0] != ' ':
        if casas[0][0] == casas[1][1] and casas[1][1] == casas[2][2]:
            check = True

    return check


def main():
    casas = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    continua = True
    cont = 0

    tabuleiro(casas)

    while continua:

        if cont == 8:
            continua = False

        jogar(cont, casas)
        tabuleiro(casas)

        cont += 1

        if cont > 4:
            if vitoria(casas):
                if cont % 2 != 0:
                    simbolo = 'X'
                else:
                    simbolo = 'O'

                print(f"Vitória! '{simbolo}' ganhou a partida!")
                continua = False


if __name__ == '__main__':
    main()

