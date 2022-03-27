# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.
#
# Составляющие проекта:
#
# Целые числа (тип int);
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл for;
# Написание пользовательских функций;
# Работа с модулем random для генерации случайных чисел.


import random

const_digits = '0123456789'
const_lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
const_uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
const_symbols = '!#$%&*+-=?@^_'
chars = []


def condition(answer, alphabet, chars):
    if answer in ("да", "д", "yes", 'y'):
        chars += [i for i in alphabet]


def mystery(answer, chars):
    a = 'il1Lo0O'
    if answer in ("да", "д", "yes", 'y'):
        for i in range(len(a)):
            if a[i] in chars:
                chars.remove(a[i])

def password_generation(chars, length, amount):
    passwords = []
    answer = ''
    for i in range(amount):
        while len(answer) < length:
            answer += chars[random.randrange(len(chars))]
        passwords.append(answer)
        answer = ''
    print(*passwords)



flag = True
print('Привет, я создаю надежные пароли.', )

while flag == True:
    amount = int(input('Сколько надежных паролей ты хочешь сгенерировать?: '))
    length = int(input('Сколько символов должно быть в пароле?: '))
    numbers = input('Используем цифры в пароле? Да \ нет?: ')
    condition(numbers, const_digits, chars)
    upper_letters = input('Прописные буквы? ABCDEFGHIJKLMNOPQRSTUVWXYZ ? Да \ нет? :')
    condition(upper_letters, const_uppercase_letters, chars)
    low_letters = input("Строчные буквы? abcdefghijklmnopqrstuvwxyz? Да \ нет?: ")
    condition(low_letters, const_lowercase_letters, chars)
    symbols = input("Символы? !#$%&*+-=?@^_ ? Да \ нет?: ")
    condition(symbols, const_symbols, chars)
    myst = input("Исключать неоднозначные символы (il1Lo0O)? Да \ нет?:  ")
    mystery(myst, chars)
    # print(chars)
    password_generation(chars, length, amount)
    chars = []
    answer = input('Сгенерировать еще пароли? Да \ нет?: ')
    if answer not in ("да", "д", "yes", 'y'):
        flag = False
print('Обязательно запишите пароли, чтобы не забыть!')
