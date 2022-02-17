n = int(input())
for i in range(n):
    k = int(input())
    while k >=0:
        #sum = sum + "2^"+ str(k)
        if k ==1:
            print("2"+" +", end=" ")
        elif k == 0:
            print("1")
        else:
            print("2^"+str(k)+" +", end=" ")
        k-=1
