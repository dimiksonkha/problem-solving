n = int(input())
for i in range(n):
    p,q,c = map(int, input().split())
    print('Result =', (p**q)%c)