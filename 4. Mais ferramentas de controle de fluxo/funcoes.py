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

def pergunta_ok(mensagem, tentativas=4, lembrete='Por favor, tente novamente!'):
    while True:
        resposta = input(mensagem)
        if resposta in {'s', 'sim', 'é'}:
            return True
        if resposta in {'n', 'não', 'nah'}:
            return False
        tentativas = tentativas - 1
        if tentativas < 0:
            raise ValueError('resposta inválida de usuário')
        print(lembrete)

pergunta_ok('Deseja continuar?')

