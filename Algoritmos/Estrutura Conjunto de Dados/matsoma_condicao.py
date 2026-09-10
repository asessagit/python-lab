# Algoritmo cria matriz 4x4 e verifica se os elementos são maiores que 10 e adiciona 2 caso sejam.

num = [[0 for j in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):
        num[i][j] = float(input(f"Digite o elemento MA[{i+1},{j+1}]: "))
        if num[i][j] > 10:
            num[i][j] += 2
print("\nMatriz resultante:")
for i in range(4):
    for j in range(4):
        print(f"{num[i][j]:.2f}", end="\t")
    print()