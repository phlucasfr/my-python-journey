def fib(n):
    """Imprime uma série de Fibonacci menor que n.""" #docstring

    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(5000)

def fib2(n):
    """Retorna uma lista contendo a série de Fibonacci até n."""

    resultado = []
    a, b = 0,1
    while a < n:
        resultado.append(a)
        a, b = b, a+b
    return resultado

f5000 = fib2(5000)
print(f5000)
