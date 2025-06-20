# sequência de Fibonacci
a, b = 0, 1 # suporta atribuição multipla
while a < 1000:

    print(a, end=',')

    a, b = b, a+b

i = 256 * 256
print('O valor de i é:', i)