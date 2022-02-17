n = int(input())
for i in range(n):
    remaining_food = float(input())
    day_counter = 0
    
    while remaining_food >= 1.0:
        remaining_food /=2
        day_counter +=1
    print(day_counter, 'days')    