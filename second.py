import math
n = 100

# Первое долгое решение
k = 3
spisok = []
while k < n:
    if k % 2 == 0:
        k += 1
    else:
        for i in range(2, int(math.sqrt(k))+1):
            if k % i == 0:
                break
        else:
            spisok.append(k)
        k += 1
print(spisok)

# Второе решение в одну строку
print([y for y in range(3, n, 2) if [z for z in range(2, int(math.sqrt(y))+1) if y % z == 0] == []])

