a = int(input())
b = input().split()
result = list(map(int, b))

answer = "NO"

for i, j in enumerate(result):
    if(i >= a):
        break
    if(i == 0):
        continue
    if(result[i] >= 0 and result[i - 1] >= 0):
        answer = "YES"
    if(result[i] < 0 and result[i - 1] < 0):
        answer = "YES"

print(answer)