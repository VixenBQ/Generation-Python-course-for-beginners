# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True если число является простым и False в противном случае.
#
#  Примечание. Следующий программный код:
#
# print(is_prime(1))
# print(is_prime(10))
# print(is_prime(17))
# должен выводить:
#
# False
# False
# True

# объявление функции
def is_prime(n):
    if n == 1:
        return False
    d = 2
    while n % d != 0:
        d += 1
    return d == n


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
