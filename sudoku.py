def sudoku():
    grade = [[0 for _ in range(9)] for _ in range(9)]
    return grade

def gradinha(grade):
    for i in range(9):
        for j in range(9):
            print(grade[i][j], end=" ")
            if (j + 1) % 3 == 0 and j != 8:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0 and i != 8:
            print("- - - - - - - - - -")

def ver_numerozinho(grade, linha, coluna, numero):
    if numero in grade[linha]:
        return True

    for i in range(9):
        if grade[i][coluna] == numero:
            return True

    bloco_linha = linha // 3
    bloco_coluna = coluna // 3
    for i in range(bloco_linha * 3, (bloco_linha + 1) * 3):
        for j in range(bloco_coluna * 3, (bloco_coluna + 1) * 3):
            if grade[i][j] == numero:
                return True

    return False

def solucao(grade):
    for i in range(9):
        linha = [grade[i][j] for j in range(9)]
        if len(set(linha)) != 9:
            return False

    for j in range(9):
        coluna = [grade[i][j] for i in range(9)]
        if len(set(coluna)) != 9:
            return False
        
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            bloco = [grade[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if len(set(bloco)) != 9:
                return False

    return True

def main():
    grade = sudoku()

    while True:
        gradinha(grade)
        linha = 0 - 1
        coluna = int(input("Digite a coluna (1-9): ")) - 1
        numero = int(input("Digite o número (1-9): "))

        if ver_numerozinho(grade, linha, coluna, numero):
            print("Número repetido! Tente novamente.")
        else:
            grade[linha][coluna] = numero

        if solucao(grade):
            print("Solução válida! Parabéns!")
            break

if __name__ == "__main__":
    main()