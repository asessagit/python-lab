# Algoritmo cria matriz 4x4 e verifica se os elementos são maiores que 10 e adiciona 2 caso sejam.
# Além disso, calcula soma, média, máximo e mínimo dos elementos.
# Função para ler um número real com validação
def ler_float(mensagem):
    while True:  # loop infinito até o usuário digitar corretamente
        valor = input(mensagem).strip()  # lê a entrada e remove espaços extras
        valor = valor.replace(",", ".")  # aceita vírgula como separador decimal, trocando por ponto
        try:
            return float(valor)  # tenta converter para número real (float)
        except ValueError:  # se não conseguir converter (entrada inválida)
            print("Entrada inválida! Digite apenas números reais (ex: 115.6).")
            # mostra mensagem de erro e volta ao início do loop

# Usuário define o tamanho da matriz
linhas = int(input("Digite o número de linhas da matriz: "))  # lê quantidade de linhas
colunas = int(input("Digite o número de colunas da matriz: "))  # lê quantidade de colunas

# Preenche a matriz com validação e aplica a regra (>10 soma 2)
num = []
for i in range(linhas):  # percorre cada linha
    linha = []
    for j in range(colunas):  # percorre cada coluna
        valor = ler_float(f"Digite o elemento MA[{i+1},{j+1}]: ")
        if valor > 10:
            valor += 2  # aplica a regra: se maior que 10, soma 2
        linha.append(valor)  # adiciona o valor na linha
    num.append(linha)  # adiciona a linha na matriz

# "Achata" a matriz em uma lista única para facilitar cálculos
todos = [elem for linha in num for elem in linha]

# Calcula estatísticas globais
soma = sum(todos)        # soma de todos os elementos
media = soma / len(todos)  # média aritmética
maximo = max(todos)      # maior valor
minimo = min(todos)      # menor valor

# Exibe os resultados
print(f"\nA soma dos elementos da matriz é: {soma:.2f}")
print(f"A média dos elementos da matriz é: {media:.2f}")
print(f"O maior elemento da matriz é: {maximo:.2f}")
print(f"O menor elemento da matriz é: {minimo:.2f}")

# Exibe a matriz com linhas de grade
print("\nMatriz resultante:")
largura = 10  # largura fixa para cada célula

def linha_horizontal():
    print("+" + "+".join("-" * largura for _ in range(colunas)) + "+")
# função auxiliar que imprime uma linha horizontal da tabela
# cada célula é representada por "-" repetido conforme a largura
# os blocos são separados por "+"

linha_horizontal()  # imprime a linha superior da tabela
for linha in num:  # percorre cada linha da matriz
    print("|" + "|".join(f"{elem:^{largura}.2f}" for elem in linha) + "|")
    # imprime os elementos da linha, centralizados dentro da largura fixa
    # cada célula é separada por "|"
    linha_horizontal()  # imprime a linha de grade abaixo da linha de dados

'''
Exemplo de entrada e saída:
Digite o número de linhas da matriz: 6
Digite o número de colunas da matriz: 6
Digite o elemento MA[1,1]: 11
Digite o elemento MA[1,2]: 11
Digite o elemento MA[1,3]: 11
Digite o elemento MA[1,4]: 11
Digite o elemento MA[1,5]: 11
Digite o elemento MA[1,6]: 11
Digite o elemento MA[2,1]: 111
Digite o elemento MA[2,2]: 111
Digite o elemento MA[2,3]: 11
Digite o elemento MA[2,4]: 11
Digite o elemento MA[2,5]: 11
Digite o elemento MA[2,6]: 11,55
Digite o elemento MA[3,1]: 15,5
Digite o elemento MA[3,2]: 11
Digite o elemento MA[3,3]: 11
Digite o elemento MA[3,4]: 11
Digite o elemento MA[3,5]: 45,9
Digite o elemento MA[3,6]: 11,99
Digite o elemento MA[4,1]: 15,98
Digite o elemento MA[4,2]: 18,7
Digite o elemento MA[4,3]: 11
Digite o elemento MA[4,4]: 111
Digite o elemento MA[4,5]: 111,01
Digite o elemento MA[4,6]: 11
Digite o elemento MA[5,1]: 111
Digite o elemento MA[5,2]: 11
Digite o elemento MA[5,3]: 111
Digite o elemento MA[5,4]: 111
Digite o elemento MA[5,5]: 11
Digite o elemento MA[5,6]: 11
Digite o elemento MA[6,1]: 11
Digite o elemento MA[6,2]: 11
Digite o elemento MA[6,3]: 1
Digite o elemento MA[6,4]: 111
Digite o elemento MA[6,5]: 11
Digite o elemento MA[6,6]: 11

A soma dos elementos da matriz é: 1309.63
A média dos elementos da matriz é: 36.38
O maior elemento da matriz é: 113.01
O menor elemento da matriz é: 1.00

Matriz resultante:
+----------+----------+----------+----------+----------+----------+
|  13.00   |  13.00   |  13.00   |  13.00   |  13.00   |  13.00   |
+----------+----------+----------+----------+----------+----------+
|  113.00  |  113.00  |  13.00   |  13.00   |  13.00   |  13.55   |
+----------+----------+----------+----------+----------+----------+
|  17.50   |  13.00   |  13.00   |  13.00   |  47.90   |  13.99   |
+----------+----------+----------+----------+----------+----------+
|  17.98   |  20.70   |  13.00   |  113.00  |  113.01  |  13.00   |
+----------+----------+----------+----------+----------+----------+
|  113.00  |  13.00   |  113.00  |  113.00  |  13.00   |  13.00   |
+----------+----------+----------+----------+----------+----------+
|  13.00   |  13.00   |   1.00   |  113.00  |  13.00   |  13.00   |
+----------+----------+----------+----------+----------+----------+
'''