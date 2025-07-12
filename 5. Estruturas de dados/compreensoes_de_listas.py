quadrados = []
for x in range(10):
    quadrados.append(x**2)
print(quadrados)

quadrados = list(map(lambda x: x**2, range(10)))
print(quadrados)

quadrados = [x**2 for x in range(10)] # mais conciso e legível
print(quadrados)

# que coisa feia
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

#equivalente
combos = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combos.append((x, y))

print(combos)