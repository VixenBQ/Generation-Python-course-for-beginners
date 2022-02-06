# #Алфавит
# Напишите программу, выводящую следующий список:
#
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# Формат выходных данных
# Программа должна вывести указанный список.
#
# Примечание. Последний элемент списка состоит из 26 символов z.

alphabet = 'abcdefghijklmnopqrstuvwxyz'
mylist = list(alphabet)
for i in range(len(mylist)):
    mylist[i] = mylist[i] * (i + 1)
print(mylist)

