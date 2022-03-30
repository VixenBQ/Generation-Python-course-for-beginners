# Переведите десятичное число 513 в двоичную систему счисления.
# BOH = Binary, Octal, Hex

num = int(input())
bin_num = bin(num)
oct_num = oct(num)
hex_num = hex(num)
answer = ''
for i in range(len(hex_num)):
    if hex_num[i].isdigit():
        answer += hex_num[i]
    elif hex_num[i].isalpha():
        answer += hex_num[i].upper()
print(bin_num[2:])
print(oct_num[2:])
print(answer[2:])

# print('{0:b}\n{0:o}\n{0:X}'.format(int(input())))