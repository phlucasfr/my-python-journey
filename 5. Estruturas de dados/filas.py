from collections import deque

fila = deque(['phelipe', 'franca', 'silva'])
fila.append('oppenha')
fila.append('hertz')

fila.popleft()
print(fila) # deque(['franca', 'silva', 'oppenha', 'hertz'])

fila.popleft()
print(fila) # deque(['silva', 'oppenha', 'hertz'])
