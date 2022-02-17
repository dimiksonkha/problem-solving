n = int(input())
for i in range(1,n+1):
    x,y,z = input().split(' ')
    print("Case %d: "%i, end="")
    if x > y:
        temp = x
        x = y
        y = temp

    if y > z:
        temp = y
        y = z
        z = temp
    
    if x > y:
        temp = x
        x = y
        y = temp

    print(x,y,z)