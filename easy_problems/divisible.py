n = int(input())
for i in range(n):
    x,y,z = map(int, input().split())
    for j in range(x,y+1):
        if j%z==0:
            print(j)
