n = int(input())

for i in range(n):
    x = str(input())
    a = int(x[len(x)-1])
    if a%2 == 0 :
        print('Even')
    else:
        print('odd') 