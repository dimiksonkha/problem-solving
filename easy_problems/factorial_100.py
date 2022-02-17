from typing import Counter


n = int(input())
for i in range(n):
    factorial = 1
    x = int(input())
    while x > 0:
        factorial *= x 
        x-=1    
    zero_counter = 0
    factorial = str(factorial)
    k = len(factorial)
    while k > 1:
        if factorial[k-1] == '0':
            zero_counter +=1   
        else:
            break
        k-=1
    if(zero_counter > 0):
        print(zero_counter)        

