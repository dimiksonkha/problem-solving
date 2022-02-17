def factorial(x):
    factorial = 1
    while x > 0:
        factorial *= x 
        x-=1    
    return factorial

n = int(input())
for i in range(n):
    m = int(input())
    sum = 0
    for j in range(1,m+1):
        sum += j/factorial(j)
    print("{:.4f}".format(sum))    
