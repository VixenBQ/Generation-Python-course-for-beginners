# Описание проекта: программа генерирует случайное число в диапазоне от 11 до 100100 и просит пользователя угадать это число. Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'. Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.
#
# Составляющие проекта:
#
# Целые числа (тип int);
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл while;
# Бесконечный цикл;
# Операторы break, continue;
# Работа с модулем random для генерации случайных чисел.

import random

count = 0
print('Добро пожаловать в числовую угадайку')

def upper_limit():
    global border, x
    border = input('Введите верхнюю границу диапазона, от 1 до _ : ')
    while border.isdigit() == False:
        border = input('Внимательнее! Введите верхнюю границу диапазона, от 1 до _ : ')
    border = int(border)
    x = random.randrange(1, border)


def is_number(answer):
    global border
    if answer.isdigit():
        if 0 < int(answer) < border:
            return True
    return False

def diapason():
    global count #border, x
    # border = int(input('Введите верхнюю границу диапазона, от 1 до _ : '))
    # x = random.randrange(1, border)

    number = input(f'Введите целое число от 1 до {border}: ')
    count += 1
    flag = is_number(number)
    while flag == False:
        print(f'А может быть все-таки введем целое число от 1 до {border}?')
        number = input('Попробуйте еще раз: ')
        count += 1
        flag = is_number(number)
    return int(number)

def game(num, x):
    global count
    while num != x:
        if num < x:
            print('Ваше число МЕНЬШЕ загаданного, попробуйте еще разок')
            num = diapason()
        elif num > x:
            print('Ваше число БОЛЬШЕ загаданного, попробуйте еще разок')
            num = diapason()
    print('Вы угадали, поздравляем!')
    print(f'Спасибо, что играли в числовую угадайку. Количество попыток: {count} ')


flag = True
while flag == True:
    upper_limit()
    print(x)
    game(diapason(), x)
    if input('Хотите сыграть еще? Да \ нет? : ').lower() not in ('y', 'yes', "д", "да", "т", "так"):
        flag = False
print('Хорошего дня! ')







