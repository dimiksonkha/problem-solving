n = int(input())
for i in range(n):
    m = int(input())
    word_list = []
    for j in range(m):
        x = input()
        word_list.append(x)

    for k in range(len(word_list)):
        
        min = word_list[k]
        index_min = k 
        for l in range(k, len(word_list)):
            if word_list[l] < min:
                min = word_list[l]
                index_min = l

        temp = word_list[k]
        word_list[k] = min
        word_list[index_min] = temp

    for word in word_list:
        print(word)  