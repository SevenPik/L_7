rows = 9
columns = 12

# Tworzymy pustą mapę/tablicę z zerami
mapa = [[0] * columns for _ in range(rows)]

# Wypełniamy mapę wartościami 1
for i in range(rows):
    for j in range(columns):
        mapa[i][j] = 0

# Przesuwamy co drugi rząd do tyłu
for i in range(1, rows, 2):
    mapa[i] = [1] + mapa[i][:-1]

for i in range(1, rows, 1):
    mapa[i] = [1] + mapa[i][:-1]


# Wyświetlamy rezultat
for row in mapa:
    print(' '.join(map(str, row)))