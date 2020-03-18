n = int(input())
i = 0
p = 0
t = 1
while(t < n):
    while(i <= p):
        t *= 2
        i += 1
    p += 1
if(t == n):
    print("YES")
else:
    print("NO")