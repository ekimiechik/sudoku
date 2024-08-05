# # # telefones = ['1234-5678', '9999-9999', '8765-4321', '8877-7788']
# # # contato = ('Yan', '1234-5678')
# # # contatos_lista = [('Yan', '1234-5678'), ('Pedro', '9999-9999'),
# # #                     ('Ana', '8765-4321'), ('Marina', '8877-7788')]

# # # print(contatos_lista[3][1])


# # minha_lista = [3, 2, 4, 5, 2]
# # for item in minha_lista:
# #     print(item)

# # my_lista = ["p*, y*, t*, h*, o*, n*"]
# # for item in my_lista:
# #     print(item)

# # for i in range(5):
# #     print(i)

# # # for i in range(3, 7):
# # #     print(i)

# # sudoku = [
# #   [9, 0, 0, 0, 8, 0, 3, 0, 0],
# #   [0, 0, 0, 2, 5, 0, 7, 0, 0],
# #   [0, 2, 0, 3, 0, 0, 0, 0, 4],
# #   [0, 9, 4, 0, 0, 0, 0, 0, 0],
# #   [0, 0, 0, 7, 3, 0, 5, 6, 0],
# #   [7, 0, 5, 0, 6, 0, 4, 0, 0],
# #   [0, 0, 7, 8, 0, 3, 9, 0, 0],
# #   [0, 0, 1, 0, 0, 0, 0, 0, 3],
# #   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# # ]

# # for numero in sudoku:
# #     print(numero)

# # import random


# # # Criei uma função que monta uma lista de listas, com isso você pode acessar oque precisar
# # def createBoard(linha, coluna, peca):
# #     armazenando_tudo = []
# #     for lista in range(linha):
# #         numeros = [random.randint(1, peca) for _ in range(coluna)]
# #         armazenando_tudo.append(numeros)
# #     return armazenando_tudo


# # # aqui chamo a função com os números que informou e armazeno em "lista_de_listas"
# # lista_de_listas = createBoard(5, 7, 20)
# # # aqui printo o conteudo dessa lista de listas
# # print(lista_de_listas)
# # # nessa parte eu seleciono a primeira lista a posição 4
# # print(lista_de_listas[0][3])

# # # #saida de exemplo foi:
# # # [[20, 11, 7, 16, 18, 13, 11]
# # # [19, 13, 16, 6, 3, 7, 10]
# # # [9, 15, 16, 4, 7, 9, 15]
# # # [6, 13, 5, 16, 12, 20, 1]
# # # [16, 9, 7, 17, 17, 4, 15]]
# # # #16

# # from collections import deque
# # pathfindingArr= [deque(['I', 'D', 'C']), deque(['C', 'J']), deque(['J', 'C', 'D', 'E'])]
# # out = []
# # for i,deq in enumerate(pathfindingArr):
# #   for element in deq:
# #     if len(out)==0:
# #       out.append(element)
# #     else:
# #       if not element == out[len(out)-1]:
# #         out.append(element)

# # valores = [-1,-2,1,2,-2,-3,4,5]
# # aux = 0
# # for atual in valores:
# #   if atual < 0:
# #     aux = 1
# #   if atual >= 0 and aux == 1:
# #     print(atual)
# #     aux = 0        
    
# # print(out)

# import tkinter as tk

# # Cria a classe para o jogo de Sudoku
# class Sudoku:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("Sudoku")
#         self.window.geometry("300x300")

#         # Cria a grade de Sudoku
#         self.grade = [[0 for _ in range(9)] for _ in range(9)]

#         # Cria os campos de entrada para os números
#         self.campos = []
#         for i in range(9):
#             linha = []
#             for j in range(9):
#                 campo = tk.Entry(self.window, width=2, font=("Arial", 24))
#                 campo.grid(row=i, column=j)
#                 linha.append(campo)
#             self.campos.append(linha)

#         # Cria o botão para verificar a solução
#         self.botao_verificar = tk.Button(self.window, text="Verificar", command=self.verificar_solucao)
#         self.botao_verificar.grid(row=10, column=0, columnspan=9)

#     def verificar_solucao(self):
#         # Lê os valores dos campos de entrada
#         for i in range(9):
#             for j in range(9):
#                 valor = self.campos[i][j].get()
#                 if valor != "":
#                     self.grade[i][j] = int(valor)

#         # Verifica se a solução é válida
#         if self.is_solucao_valida():
#             print("Solução válida!")
#         else:
#             print("Solução inválida!")

#     def is_solucao_valida(self):
#         # Verifica se cada linha tem os números de 1 a 9 sem repetição
#         for i in range(9):
#             linha = [self.grade[i][j] for j in range(9)]
#             if not self.is_linha_valida(linha):
#                 return False

#         # Verifica se cada coluna tem os números de 1 a 9 sem repetição
#         for j in range(9):
#             coluna = [self.grade[i][j] for i in range(9)]
#             if not self.is_linha_valida(coluna):
#                 return False

#         # Verifica se cada bloco 3x3 tem os números de 1 a 9 sem repetição
#         for i in range(0, 9, 3):
#             for j in range(0, 9, 3):
#                 bloco = [self.grade[x][y] for x in range(i, i+3) for y in range(j, j+3)]
#                 if not self.is_linha_valida(bloco):
#                     return False

#         return True

#     def is_linha_valida(self, linha):
#         # Verifica se a linha tem os números de 1 a 9 sem repetição
#         return sorted(linha) == list(range(1, 10))

#     def run(self):
#         self.window.mainloop()

# # Cria uma instância do jogo de Sudoku e executa
# sudoku = Sudoku()
# sudoku.run()

# Função para imprimir a grade de Sudoku
# def imprimir_grade(grade):
#     for i in range(9):
#         for j in range(9):
#             print(grade[i][j], end=" ")
#             if (j + 1) % 3 == 0 and j != 8:
#                 print("|", end=" ")
#         print()
#         if (i + 1) % 3 == 0 and i != 8:
#             print("- - - - - - - - - -")

# # Função para verificar se a solução é válida
# def is_solucao_valida(grade):
#     # Verifica se cada linha tem os números de 1 a 9 sem repetição
#     for i in range(9):
#         linha = [grade[i][j] for j in range(9)]
#         if not is_linha_valida(linha):
#             return False

#     # Verifica se cada coluna tem os números de 1 a 9 sem repetição
#     for j in range(9):
#         coluna = [grade[i][j] for i in range(9)]
#         if not is_linha_valida(coluna):
#             return False

#     # Verifica se cada bloco 3x3 tem os números de 1 a 9 sem repetição
#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             bloco = [grade[x][y] for x in range(i, i+3) for y in range(j, j+3)]
#             if not is_linha_valida(bloco):
#                 return False

#     return True

# # Função para verificar se uma linha é válida
# def is_linha_valida(linha):
#     # Verifica se a linha tem os números de 1 a 9 sem repetição
#     return sorted(linha) == list(range(1, 10))

# # Função principal
# def main():
#     # Cria a grade de Sudoku
#     grade = [[0 for _ in range(9)] for _ in range(9)]

#     # Pede ao usuário para preencher a grade
#     for i in range(9):
#         for j in range(9):
#             while True:
#                 valor = input(f"Digite o valor para a posição ({i+1},{j+1}): ")
#                 if valor.isdigit() and 1 <= int(valor) <= 9:
#                     grade[i][j] = int(valor)
#                     break
#                 else:
#                     print("Valor inválido. Por favor, digite um número entre 1 e 9.")

#     # Imprime a grade preenchida
#     print("Grade preenchida:")
#     imprimir_grade(grade)

#     # Verifica se a solução é válida
#     if is_solucao_valida(grade):
#         print("Solução válida!")
#     else:
#         print("Solução inválida!")

# # Executa a função principal
# if __name__ == "__main__":
#     main()

# def verificar_sudoku(grade):
#     # Verifica se cada linha tem números repetidos
#     for linha in grade:
#         if len(set(linha))!= 9:
#             return False

#     # Verifica se cada coluna tem números repetidos
#     for coluna in zip(*grade):
#         if len(set(coluna))!= 9:
#             return False

#     # Verifica se cada bloco 3x3 tem números repetidos
#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             bloco = [grade[x][y] for x in range(i, i+3) for y in range(j, j+3)]
#             if len(set(bloco))!= 9:
#                 return False

#     return True

# # Exemplo de uso
# grade = [
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]

# if verificar_sudoku(grade):
#     print("Sudoku válido!")
# else:
#     print("Sudoku inválido!")

def criar_grade():
    grade = [[0 for _ in range(9)] for _ in range(9)]
    return grade

def imprimir_grade(grade):
    for i in range(9):
        for j in range(9):
            print(grade[i][j], end=" ")
            if (j + 1) % 3 == 0 and j != 8:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0 and i != 8:
            print("- - - - - - - - - -")

def verificar_numero_repetido(grade, linha, coluna, numero):
    # Verifica se o número já existe na linha
    if numero in grade[linha]:
        return True

    # Verifica se o número já existe na coluna
    for i in range(9):
        if grade[i][coluna] == numero:
            return True

    # Verifica se o número já existe no bloco 3x3
    bloco_linha = linha // 3
    bloco_coluna = coluna // 3
    for i in range(bloco_linha * 3, (bloco_linha + 1) * 3):
        for j in range(bloco_coluna * 3, (bloco_coluna + 1) * 3):
            if grade[i][j] == numero:
                return True

    return False

def verificar_solucao_valida(grade):
    # Verifica se cada linha tem os números de 1 a 9 sem repetição
    for i in range(9):
        linha = [grade[i][j] for j in range(9)]
        if len(set(linha)) != 9:
            return False

    # Verifica se cada coluna tem os números de 1 a 9 sem repetição
    for j in range(9):
        coluna = [grade[i][j] for i in range(9)]
        if len(set(coluna)) != 9:
            return False

    # Verifica se cada bloco 3x3 tem os números de 1 a 9 sem repetição
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            bloco = [grade[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if len(set(bloco)) != 9:
                return False

    return True

def main():
    grade = criar_grade()

    while True:
        imprimir_grade(grade)
        linha = int(input("Digite a linha (1-9): ")) - 1
        coluna = int(input("Digite a coluna (1-9): ")) - 1
        numero = int(input("Digite o número (1-9): "))

        if verificar_numero_repetido(grade, linha, coluna, numero):
            print("Número repetido! Tente novamente.")
        else:
            grade[linha][coluna] = numero

        if verificar_solucao_valida(grade):
            print("Solução válida! Parabéns!")
            break

if __name__ == "__main__":
    main()