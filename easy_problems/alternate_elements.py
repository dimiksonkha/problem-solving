n = int(input())
for i in range(n):
    numbers = list(map(int, input().split()))
    for j in range(1,len(numbers),2):
        print(j,end=" ")