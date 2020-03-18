a = int(input())
b = input().split()
result = list(map(int, b))

for i, j in enumerate(result):
    if(i >= a):
        break
    if(j % 2 == 0):
        print(j, end = " ")