n = int(input())
for i in range(n):
    arr = map(int, input().split(' '))
    array = list(arr)
    other_total_run = array[0]
    own_total_run = array[1]
    remaining_ball = array[2]
    current_run_rate = own_total_run / ((300-remaining_ball)/6)
    asking_run_rate = (other_total_run +1 - own_total_run)/(remaining_ball/6)
    print('%0.2f %0.2f' %(current_run_rate,asking_run_rate))