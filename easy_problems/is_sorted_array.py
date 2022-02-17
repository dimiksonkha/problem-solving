def is_sorted_array(array):
    is_sorted = False
    is_asc_sorted = True
    is_desc_sorted = True
    
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            is_asc_sorted = False
            break
    
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            is_desc_sorted = False
            break
    if is_asc_sorted or is_desc_sorted:
        is_sorted = True

    return is_sorted
 
n = int(input())
for i in range(n):
    m = int(input())
    array = []
    for j in range(m):
        x = int(input())
        array.append(x)
    if is_sorted_array(array):
        print('YES')
    else:
        print('NO')        

