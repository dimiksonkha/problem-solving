n = int(input())
for i in range(1,n+1):
    x = int(input())
    print("Case %d: "%i, end="")
    for j in range(1,x+1):
        if x%j == 0:
            print(j, end=" ")
    print()        
