n = int(input())
for i in range(n):
    x = float(input())
    digit_counter = 1
    while x/10 > 1:
        x = x/10
        digit_counter+=1
    print(digit_counter)    
  