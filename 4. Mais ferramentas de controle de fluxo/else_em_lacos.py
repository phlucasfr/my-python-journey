for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'igual a', x, '*', n//x)
            break
    else: # pertence ao laço for, não à instrução if
        # a iteração passou direto sem encontrar um fator
        print(n, 'é um número primo')