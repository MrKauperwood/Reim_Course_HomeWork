spisok = [1, 2, 3, "sd"]
#spisok = [1, 1, 1, 1, 1, 1]

print(len(set(spisok)) == 1)
print([spisok[0]]*len(spisok) == spisok)
print(spisok.count(spisok[0]) == len(spisok))


