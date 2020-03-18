a = int(input())
b = input().split()
result = list(map(int, b))

counter = 0

for i, j in enumerate(result):
    if(i >= a):
        break
    if(i == 0 or i == a-1):
        continue
    if(result[i] > result[i-1] and result[i] > result[i+1]):
        counter += 1

print(counter)        