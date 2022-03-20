# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.
#
# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
#
#  Примечание 2. Следующий программный код:
#
# print(get_next_prime(6))
# print(get_next_prime(7))
# print(get_next_prime(14))
# должен выводить:
#
# 7
# 11
# 17

def is_prime(n):
    if n == 1:
        return False
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def get_next_prime(num):
    num += 1
    while is_prime(num) != True:
        num += 1
        is_prime(num)
    print(num)


get_next_prime(int(input()))

#     for i in range(2, num + 1):
#         if is_prime(i) == True:
#             print(i)
#             break
# num = int(input())
# print(get_next_prime(num))
