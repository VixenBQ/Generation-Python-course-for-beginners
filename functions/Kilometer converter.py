# Конвертер километров
# Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях. Формула для преобразования: мили = километры * 0.6214.
#
# Примечание. Следующий программный код:
#
# print(convert_to_miles(1))
# print(convert_to_miles(5))
# print(convert_to_miles(10))
# должен выводить:
#
# 0.6214
# 3.107
# 6.214

def convert_to_miles(kilometers):
    return kilometers * 0.6214


km = float(input())
print(convert_to_miles(km))
