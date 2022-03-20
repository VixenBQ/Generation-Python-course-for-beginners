# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.
#
#  Примечание. Следующий программный код:
#
# print(is_one_away('bike', 'hike'))
# print(is_one_away('water', 'wafer'))
# print(is_one_away('abcd', 'abpo'))
# print(is_one_away('abcd', 'abcde'))
# должен выводить:
#
# True
# True
# False
# False

# def is_one_away(word1, word2):
#     diff = 0
#     if len(word1) == len(word2):
#         for i in range(len(word1)):
#             if word1[i] != word2[i] and diff <= 1:
#                 diff += 1
#     if diff == 1:
#         return True
#     else:
#         return False
#
# def is_one_away(word1, word2):
#     return len([i for i in word1 if i not in word2]) == 1 and len(word1) == len(word2)

def is_one_away(word1, word2):
    a = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            a += 1
    return len(word1) == len(word2) and a == 1


word1, word2 = input(), input()
print(is_one_away(word1, word2))
