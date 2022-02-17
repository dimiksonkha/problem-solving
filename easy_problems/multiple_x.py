n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    j = 1
    while j*x <=y:
        print(j*x)
        j+=1
