
n = int(input())
for i in range(n):
    t = map(int, input().split(' '))
    x = list(t)
    
    counter = 0
    for j in range(x[0],x[1]):
        is_prime = True
        for k in range(2,j):
            if j%k == 0:
                is_prime = False       
        if(is_prime):
             counter+=1     
    print(counter)                 