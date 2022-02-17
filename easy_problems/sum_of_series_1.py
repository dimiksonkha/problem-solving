n = int(input())
for i in range(n):
    x,k = map(int,input().split())
    sum = 0
    for j in range(k+1):
        sum += x ** j
    print("Result =", sum)
