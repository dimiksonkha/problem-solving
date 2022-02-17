n = int(input())
for i in range(n):
    factorial = 1
    x = int(input())
    while x > 0:
        factorial *= x 
        x-=1    
    print(factorial)
