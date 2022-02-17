n = int(input())

def gcd(a,b):
    while b !=0 :
        temp = b
        b = a%b
        a = temp
    return a

for i in range(n):
    x = map(int, input().split())
    numbers = list(x)
    print(numbers)
    lcm = int((numbers[0]* numbers[1])/gcd(numbers[0],numbers[1]))
    print("LCM =", lcm)


