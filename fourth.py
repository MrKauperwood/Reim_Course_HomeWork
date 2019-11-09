a = 9  # Строки
b = 9  # Столбцы
kol_vo_steps = 3 # Количество шагов

stroka_original = "...............................@.......@@@......................................."
# stroka_original = "..............................@@@......@@@......................................."
# stroka_original = "......................................@@@@@......................................"
# stroka_original = ".......................................@@@......................................."
dlina = len(stroka_original)



def print_field(string_for_print):
    k = 0
    for i in range(a):
        for j in range(b):
            print(string_for_print[k], end="")
            k += 1
        print()


def next_step(stroka):
    global stroka_original
    next_stroka = ""
    for i in range(len(stroka)):
        current_symbol = stroka[i]
        count = 0

        if (i + 1) >= dlina:
            if stroka[i + 1 - dlina] == "@": count += 1
        elif (i + 1) < dlina:
            if stroka[i + 1] == "@": count += 1

        if (i - 1) < 0:
            if stroka[i - 1 + dlina] == "@": count += 1
        elif (i - 1) >= 0:
            if stroka[i - 1] == "@": count += 1

        if (i + b) >= dlina:
            if stroka[i + b - dlina] == "@": count += 1
        elif (i + b) < dlina:
            if stroka[i + b] == "@": count += 1

        if (i + b + 1) >= dlina:
            if stroka[i + b + 1 - dlina] == "@": count += 1
        elif (i + b + 1) < dlina:
            if stroka[i + b + 1] == "@": count += 1

        if (i + b - 1) >= dlina:
            if stroka[i + b - 1 - dlina] == "@": count += 1
        elif (i + b - 1) < dlina:
            if stroka[i + b - 1] == "@": count += 1

        if (i - b) < 0:
            if stroka[i - b + dlina] == "@": count += 1
        elif (i - b) >= 0:
            if stroka[i - b] == "@": count += 1

        if (i - b + 1) < 0:
            if stroka[i - b + 1 + dlina] == "@": count += 1
        elif (i - b + 1) >= 0:
            if stroka[i - b + 1] == "@": count += 1

        if (i - b - 1) < 0:
            if stroka[i - b - 1 + dlina] == "@": count += 1
        elif (i - b - 1) >= 0:
            if stroka[i - b - 1] == "@": count += 1

        if (current_symbol == ".") and count == 3:
            current_symbol = "@"
        elif (current_symbol == "@") and (count != 2) and (count != 3):
            current_symbol = "."

        next_stroka += current_symbol
    stroka_original = next_stroka


i = 0
while i < kol_vo_steps:
    print_field(stroka_original)
    next_step(stroka_original)
    print()
    i += 1
