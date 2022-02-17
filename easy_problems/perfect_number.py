def is_perfact_number(x):
    sum = 0
    for q in range(1,x):
        if x % q == 0:
            sum+=q
    if sum == x:
        return True
    else:
        return False

n = int(input())
for i in range(n):
    x = int(input())
    if is_perfact_number(x):
        print('YES,' + str(x) + ' is perfect number')
    else:
        print('NO,' + str(x) + ' is not a perfect number')    

