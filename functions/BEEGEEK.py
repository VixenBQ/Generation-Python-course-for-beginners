# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
#
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.
#
#  Примечание. Следующий программный код:
#
# print(is_valid_password('1221:101:22'))
# print(is_valid_password('565:30:50'))
# print(is_valid_password('112:7:9'))
# print(is_valid_password('1221:101:22:22'))
#
# должен выводить:
#
# True
# False
# False
# False


def true_password(password):
    password_split = password.split(':')
    a, b, c = password_split[0], int(password_split[1]), int(password_split[2])
    a = [i for i in a]
    a_revers = a[::-1]
    return len(password_split) == 3 and a == a_revers and c % 2 == 0 and [i for i in range(1, b + 1) if b % i == 0] == [1, b]


password = input()
print(true_password(password))
