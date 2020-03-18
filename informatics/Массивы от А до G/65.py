a = int(input())
b = input().split()
result = list(map(int, b))

counter = 0

for i, j in enumerate(result):
    if(i >= a):
        break
    if(j > 0):
        counter += 1

print(counter)