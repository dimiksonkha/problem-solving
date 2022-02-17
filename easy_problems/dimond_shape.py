t = int(input())
for i in range(t):
    n,m=map(int, input().split())
    k=1
    while n !=0:
        print(str(m)*k,end=" ")
        print()
        if k == n:
            k-=1
            n-=1
        else:
            k+=1    


        
        