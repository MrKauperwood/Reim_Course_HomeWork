# Задайте тут свои параметры
num_lines = 25
num_cols = 200
hor_side = 4
ratio = 3

try:
    mas = [i for i in range(1, num_lines + 1, hor_side - 1) if i <= num_lines]
    str1 = " " * (hor_side - 1) + (hor_side) * "*" + " " * (hor_side + (hor_side - 2))
    str1_copy = " " * (hor_side - 1) + (hor_side) * "*" + " " * (hor_side + (hor_side - 2))

    count = 2
    k = 0

    for line in range(1, num_lines + 1):
        if line in mas:
            if mas.index(line) % 2 != 0:
                stroka = ""
                i = 2 * hor_side - 2
                while len(stroka) <= num_cols:
                    if i == len(str1) - 1:
                        i = 0
                    if str1[i] == " ":
                        stroka += (str1[i] * ratio)
                    else:
                        stroka += (str1[i] + " " * (ratio - 1))
                    i += 1
                print(stroka)
                k = 0
                str1_copy = str1
            else:
                stroka = ""
                i = 0
                t = 1
                while len(stroka) <= num_cols:
                    if i == len(str1) - 1:
                        i = 0
                    if str1[i] == " ":
                        stroka += (str1[i] * (ratio))
                    else:
                        stroka += (str1[i] + " " * (ratio - 1))
                    i += 1
                print(stroka)
                k = 1
                str1_copy = str1
        else:
            if k == 1:
                str2 = str1_copy[1:hor_side + 1] + str1_copy[hor_side - 1:-1]
                first = str2.find("*")
                second = str2.rfind("*")
                str2 = str2[:first + 1] + " " * (second - first - 1) + str2[second:]
                str1_copy = str2
                stroka = ""
                i = 0
                while len(stroka) <= num_cols:
                    if i == len(str2) - 1:
                        i = 0
                    if str2[i] == " ":
                        stroka += (str2[i] * ratio)
                    else:
                        stroka += (str2[i] + " " * (ratio - 1))
                    i += 1
                print(stroka)

            else:
                p = 0
                str2 = str1_copy[1:hor_side + 1] + str1_copy[hor_side - 1:-1]
                str3 = ""
                for i in str2:
                    if i == " ":
                        str3 += "*"
                    else:
                        str3 += " "
                str1_copy = str2
                str3 = str3.replace(" *", "**")
                str3 = str3.replace("* ", "**")

                str4 = ""
                i = 2 * hor_side - 2
                while len(str4) < len(str3):
                    if i == len(str3) - 1:
                        i = 0
                    str4 += str3[i]
                    i += 1

                first = str4.find("*")
                second = str4.rfind("*")
                str4 = str4[:first + 1] + " " * (second - first - 1) + str4[second:]

                stroka = ""
                i = 0
                while len(stroka) <= num_cols:
                    if i == len(str3) - 1:
                        i = 0
                    if str4[i] == " ":
                        stroka += (str4[i] * ratio)
                    else:
                        stroka += (str4[i] + " " * (ratio - 1))
                    i += 1
                print(stroka)

except Exception:
    print("\nВы ввели невалидные входные данные!\nПроверьте их и исправьте.\n")
    print("  hor_side > 1 (так как шестиугольников с длиной стороны <=1 быть в природе проcто не может!)")
    print("  ratio    > 0")
