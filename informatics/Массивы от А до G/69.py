a = int(input())
b = input().split()

array = list(map(int, b))

newArr = []

for i, j in enumerate(array):
    if(i < a):
        newArr.append(j)

for i in reversed(newArr):
    print(i, end = " ")