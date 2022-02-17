n = int(input())
for i in range(n):
    sentence = input()
    search_char = input()
    char_counter = 0
    for q in sentence:
        if q == search_char:
            char_counter +=1
    if char_counter == 0:
        print("'"+search_char+"'" + ' is not present')
    else:
        print('occurance of ' + "'"+search_char+"'"  + ' in ' + "'"+sentence+"'" + ' = ' + str(char_counter))            