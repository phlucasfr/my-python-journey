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

def loja_de_queijos(tipo, *argumentos, **argumentos_nomeados):
    print("-- Você tem algum", tipo, "?")
    print("-- Lamento, acabou o", tipo)
    for arg in argumentos:
        print(arg)
    print("-" * 40)
    for kw in argumentos_nomeados:
        print(kw, ":", argumentos_nomeados[kw])

loja_de_queijos("Limburger", "Está muito mole, senhor",
           "Está realmente muito, MUITO mole, senhor.",
           vendedor="Michael Palin",
           cliente="John Cleese",
           sketch="Sketch da Loja de Queijos")

def f(pos1, pos2, /, pos_ou_kwd, *, kwd1, kwd2):
    pass

# Se / e * não estão presentes na definição da função, 
# argumentos podem ser passados para uma função por posição ou por nome.

def arg_padrao(arg):
    print(arg)

arg_padrao("posicional")
arg_padrao(arg="nomeado")

def somente_posicional(arg, /):
    print(arg)

somente_posicional("somente posicional")

def somente_nomeado(*, arg):
    print(arg)

somente_nomeado(arg="somente nomeado")

def concat(*args, sep="/"):
    print(sep.join(args))

concat("terra", "marte", "vênus")
concat("terra", "marte", "vênus", sep=".")

print(list(range(3,6)))

args = [3, 6]
print(list(range(*args)))

def cria_incrementador(n):
    return lambda x: x + n

f = cria_incrementador(42)
print(f(0))
print(f(1))

def minha_função():

    """Não faça nada, mas documente o fato.


    Não, é sério, ela faz nada mesmo.

    """

    pass

print(minha_função.__doc__)


