quadrados = [1, 4, 9, 16, 25]

print(quadrados[0])

# também suportam concatenação
quadrados + [36, 49, 64, 81, 100]
print(quadrados)

# listas são mutáveis
cubos = [1, 8, 27, 65, 125]
cubos[3] = 64
print(cubos)

# permitido append no final da lista
cubos.append(216)
cubos.append(7 ** 3)
print(cubos)

# atribuição simples por referência 
rgb = ["Vermelho", "Verde", "Azul"]
rgba = rgb

print(id(rgb)== id(rgba))

rgba.append("Alfa")
print(rgb)
print(rgba)

# listas suportam fatiamento
print(rgba[1:])

# atribuição pro fatiamento
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letras[2:5] = ['C', 'D', 'E']
print(letras)

print(len(letras))

# aninhamento de listas
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x)