n = input()
power = len(n)
sum = 0
for i in range(power):
    x = int(n[i])**power
    sum = sum + x

if sum == int(n):
    print(n," is an armstrong number")
else:
    print(n," is not an armstrong number")        
