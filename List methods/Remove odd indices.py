# Удалите нечетные индексы
# На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список в соответствии с условием задачи.
#
#  Примечание. Используйте оператор del.

num_list = []
for i in range(int(input())):
    num_list.append(int(input()))
del num_list[1::2]
print(num_list)