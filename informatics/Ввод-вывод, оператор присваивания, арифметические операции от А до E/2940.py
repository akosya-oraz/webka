s = 109
v = int(input())
t = int(input())

if(v < 0):
    km = 109+(v*t)
else:    
    km = v*t
print(km%s)