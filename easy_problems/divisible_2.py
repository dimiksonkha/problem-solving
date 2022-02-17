n = int(input())
for i in range(n):
    x,y,z = map(int, input().split())
    divisor = x*y
    for j in range(1,z):
        if j % divisor==0:
            print(j)