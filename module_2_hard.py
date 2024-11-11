num = int(input('Ввод числа: ',))
def get_shifr(cod):
    shifr = ''
    for i in range(1,cod):
        for j in range(1,cod):
            if i > j:
                continue
            if cod % (i + j) == 0:
                shifr = shifr + str(i) + str (j)
    return shifr
print('Шифр:', get_shifr(num))

