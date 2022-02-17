import math
n = int(input())
for i in range(n):
    a,b,c = map(int, input().split())
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print('Area = ' + "{:.3f}".format(area))
