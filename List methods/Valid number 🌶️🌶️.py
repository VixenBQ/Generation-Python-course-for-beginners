# На вход программе подается строка текста. Напишите программу, которая определяет является ли введенная строка корректным телефонным номером. Строка текста является корректным телефонным номером если она имеет формат:
#
# abc-def-hijk или
# 7-abc-def-hijk
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести «YES» если строка является корректным телефонным номером и «NO» в противном случае.
#
# Примечание. Телефонный номер должен содержать только цифры и символ -, а количество цифр в каждой группе должны быть правильным.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 7-301-447-5820
# Sample Output 1:
#
# YES
# Sample Input 2:
#
# 301-447-5820
# Sample Output 2:
#
# YES
# Sample Input 3:
#
# 301-4477-5820
# Sample Output 3:
#
# NO
# Sample Input 4:
#
# 3X1-447-5820
# Sample Output 4:
#
# NO
# Sample Input 5:
#
# 3014475820
# Sample Output 5:
#
# NO


origin = input()
origin_split = origin.split('-')
work = origin.replace('-', '')
pattern = [3, 3, 4]
pattern_7 = [1, 3, 3, 4]
len_of_elem_origin = []
if work.isdigit() == False:
    print('NO')
else:
    for i in range(len(origin_split)):
        len_of_elem_origin.append(len(origin_split[i]))
    if len(len_of_elem_origin) == 4 and origin[0] == '7' and len_of_elem_origin == pattern_7:
        print('YES')
    elif len_of_elem_origin == pattern:
        print('YES')
    else:
        print('NO')


# n = input().replace('-', '0')
# if n[0] == '7' and n.isdigit() and len(n) == 14:
#     print("YES")
# elif n.isdigit() and len(n) == 12:
#     print("YES")
# else:
#     print("NO")
