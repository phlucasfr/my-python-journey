for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} igual a {x} * {n//x}")
            break

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Encontrado um número par {num}")
        continue
    print(f"Encontrado um número impar {num}")
