number_list = [1,2,2,1,5,5,5,5,1,10,1,2,4]
new_number_list = [1,2,2,1,5,5,5,5,1,10,1,2,4]
n = len(number_list)

for i in range(n):
    
    num_counter = 0
    index = 0
    for num in number_list:
        if num == new_number_list[i]:
            num_counter += 1
            if num_counter >=2:
                number_list.pop(index)
        index += 1        
    
print(number_list)
