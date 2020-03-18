import math
x1 = int(input())
x2 = int(input())
for i in range(x1, x2+1):
    if(i == (int(math.sqrt(i)) ** 2)):
        print(i)