import math
n = 10

# Первое долгое решение
k = 2
spisok = []
while k < n:
    if (k % 2 == 0) and (k!=2):
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
print([y for y in range(2, n) if (y==2) or (y%2!=0) and [z for z in range(2, int(math.sqrt(y))+1) if y % z == 0] == []])
