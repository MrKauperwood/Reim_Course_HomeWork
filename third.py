#num_lines = int(input("Введите количество строк\n"))
#num_cols = int(input("Введите количество колонок\n"))
#hor_side = int(input("Введите длину стороны соты\n"))
#ratio = int(input("Введите соотношение звездочек и пробелов\n"))

num_lines = 12
num_cols = 15
hor_side = 3

mas = [i*2+1 for i in range(0, num_lines) if i*2+1 <= num_lines]

for line in range(1,num_lines+1):
    if line in mas:
        str1 = "."*(hor_side-1)+ hor_side*"*" + "."*(hor_side+1)
        if mas.index(line) % 2 != 0:
            stroka = ""
            i = 2*hor_side-2
            while len(stroka) <= num_cols:
                if i == len(str1) - 1:
                    i = 0
                stroka += str1[i]
                i += 1
            print(stroka)
        else:
            stroka = ""
            i = 0
            while len(stroka) <= num_cols:
                if i == len(str1) - 1:
                    i = 0
                stroka += str1[i]
                i += 1
            print(stroka)
    else:
        print()

print(mas)

