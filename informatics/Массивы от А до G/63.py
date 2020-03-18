m = int(input())
n = input().split()
arr = list(map(int, n))
for i, j in enumerate(arr):
    if(i >= m):
        break
    if(i % 2 == 0):
        print(j, end = " ")