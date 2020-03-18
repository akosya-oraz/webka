n = int(input())
p = 0
i = 0
t = 1
while(t <= n):
    print(t, end = " ")
    while(i <= p):
        t *= 2
        i += 1
    p += 1

