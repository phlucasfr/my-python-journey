matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# que coisa feia
print([[linha[i] for linha in matriz] for i in range(4)])

# equivale a isso
transposta = []
for i in range(4):
    linha_transposta = []

    for linha in matriz:

        linha_transposta.append(linha[i])

    transposta.append(linha_transposta)
