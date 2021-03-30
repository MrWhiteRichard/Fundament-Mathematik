import numpy as np

gamma = 0.9

t = np.array([
    [5, 4, 3, 2, 1],
    [4, 3, 2, 1, 0],
    [5, 4, 3, 2, 1],
    [6, 5, 4, 3, 5],
    [7, 6, 5, 4, 6]
])

r = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5],
    [0, 0, 0, 0, gamma * 5],
])

v_ast = r + 10 * gamma ** t /  (1 - gamma ** 5)
v_ast = np.rot90(v_ast)
v_ast = np.round(v_ast, decimals = 3)

print('#', '-'*64, '#', '\n')
print(v_ast, '\n')
print('#', '-'*64, '#', '\n')