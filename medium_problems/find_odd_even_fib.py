"""
Find total number of oddfibonacci numbers and total number of evenfibonacci numbers 
between Nth fibonacci number and Mth fibonacci number

"""
import math
t = int(input())
for i in range(t):

    n,m=map(int,input().split())

    fib_numbers = [ int((1.618034 ** x - (1-1.618034) ** x)/ math.sqrt(5)) for x in range(n-1,m)]

    odd_fib_count, even_fib_count = 0,0
    for num in fib_numbers:
        if num == 0 or num %2 == 0:
            even_fib_count+=1
        else:
            odd_fib_count+=1

    print("Case %d:" %(i+1))
    print("Odd = ", odd_fib_count)
    print("Even = ", even_fib_count)

