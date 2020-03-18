import math
x = int(input())
c = 0
for i in range(1, int(math.sqrt(x))):
    if(x % i == 0):
        c += 1

c *= 2
if(x % math.sqrt(x) == 0):
    c += 1

print(c)