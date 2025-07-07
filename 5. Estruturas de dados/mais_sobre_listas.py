a = [1, 2, 3, 4, 5]
a.append(6)
print(a) # [1, 2, 3, 4, 5, 6]

a.extend(a)
print(a) # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

a.insert(0, 0)
print(a) # [0, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

a.remove(6)
print(a) # [0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]

a.pop(0)
print(a) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]

a.clear()
print(a) # []

print(a.count(0)) # 0

a = [1, 2, 3, 4, 5]
a.sort(key=None, reverse=True)
print(a) # [5, 4, 3, 2, 1]

a.reverse()
print(a) # [1, 2, 3, 4, 5]

b = a.copy()
print(b) # [1, 2, 3, 4, 5]
