n = int(input())
answer = ''
while n >=1:
    answer = str(n%2) + answer
    n = n//2
print(answer)