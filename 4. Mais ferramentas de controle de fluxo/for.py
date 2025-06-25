palavras = ['gato', 'janela', 'defenestrar']
for p in palavras:
    print(p, len(p))

# gato 4
# janela 6
# defenestrar 11

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# iterar por uma cópia, por segurança
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)
    