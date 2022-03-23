# Змеиный регистр
# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».
#
# Примечание 1. Почитать подробнее о стилях именования можно тут.
#
# Примечание 2. Следующий программный код:
#
# print(convert_to_python_case('ThisIsCamelCased'))
# print(convert_to_python_case('IsPrimeNumber'))
# должен выводить:
#
# this_is_camel_cased
# is_prime_number

def convert_to_python_case(text):
    result = ''
    for i in range(len(text)):
        if text[i].isupper() and i == 0:
            result += text[i].lower()
        elif text[i].isupper():
            result += '_' + text[i].lower()
        else:
            result += text[i]
    return result

# def convert_to_python_case(text):
#     return ''.join(['_' + symbol.lower() if symbol.isupper() else symbol for symbol in text])[1:]

text = input()
print(convert_to_python_case(text))
