# #Суммы двух
# На вход программе подается натуральное число n \ge 2n≥2, а затем nn целых чисел. Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (00 и 11, 11 и 22, 22 и 33 и т.д.).
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список, состоящий из сумм соседних чисел.

n = int(input())
my_list = []
for i in range(n):
    my_list.append(int(input()))
your_list = []
for i in range(0, len(my_list)):
    if i !=0:
        your_list.append((my_list[i] + my_list[i - 1]))
print(your_list)
n = int(input())

####
n, a = int(input()), int(input())
lst = []
for _ in range(n-1):
    b = int(input())
    lst.append(a + b)
    a = b
print(lst)
####

