# Звездный треугольник 1
# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 1010 в соответствии с образцом:
#
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
# Примечание. Для вывода треугольника используйте цикл for.

# объявление функции
def draw_triangle():
    for i in range(10):
        print((i + 1) * '*')

# основная программа
draw_triangle()  # вызов функции
