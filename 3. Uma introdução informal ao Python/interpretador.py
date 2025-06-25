# este é o primeiro comentário
spam = 1 
texto = "# Este não é um comentário por estar entre aspas"

# Hello flat earth example kkk
o_mundo_é_plano = True
if o_mundo_é_plano:
    print("Cuidado para não cair da borda!")

print(17 / 3) # divisão clássica retorna um ponto flutuante
print(17 // 3) # divisão pelo piso descarta a parte fracionária
print(17 % 3) # retorna o resto da divisão

print(5 ** 2) # python suporta calculo de potência

# operador '=' para atribuição em python
largura = 20

# exemplo de variavel não definida
# n

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'n' is not defined

# operadores com operandos de diferentes tipos convertem o inteiro para ponto flutuante:
print(4 * 3.75 - 1)
# 14.0

print('spam eggs') # aspas simples
print("Coelho de Paris, eu te projeto :)! Viva!") # aspas duplas

print('d\'água') # usar \' para escapar a aspa simples...
print("d'água") # ou usar aspas duplas
print('"Sim", eles disseram')
print("\"Sim\", eles disseram")

print(r'C:\algum\nome')  # observar o r antes das aspas

#strings literais 
print("""\
    Uso: coisinha [OPÇÕES]
        -h                        Exibe esta mensagem de uso
        -H hostname               Hostname para se conectar
      """)

print(3 * 'un' + 'ium') # Strings podem ser concatenadas (coladas) com o operador +, e repetidas com *

print('Py' 'thon') # Contatenação automagica

prefixo = 'Py'

print(prefixo + 'thon')

palavra = 'Python'
print(palavra[0]) #Indexação

print(palavra[:2]) # Fatiamento

#strings em python são imutáveis

s = 'supercalifragilisticexpialidoce'
print(len(s)) # comprimento de uma string

