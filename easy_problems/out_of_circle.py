import math
n = int(input())
for i in range(n):
    x1,y1 = map(int, input().split())
    r = int(input())
    x2,y2 = map(int, input().split())
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    if distance > r:
        print('The point is not  inside the circle')
    else:
        print("The point is inside the circle")    