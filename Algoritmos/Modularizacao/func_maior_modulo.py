
def MaiorModulo(VetNum):
    if VetNum is None or len(VetNum) == 0:
        print("Erro: O vetor está vazio ou não foi fornecido.")
        return
    if len(VetNum) == 1:
        return VetNum[0]
    maior = VetNum[0]  # Inicializa o maior com o primeiro elemento
    for i in range(1, len(VetNum)):
            if abs(VetNum[i]) > abs(maior):
                maior = VetNum[i]
    return maior

# Main program
VetInicial = list(map(int,input("Digite os números serparados por espaço: ").split()))
M = MaiorModulo(VetInicial)
print(M)
