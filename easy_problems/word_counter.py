n = int(input())
for i in range(n):
    sentence = input()
    word_counter = 1
    for q in sentence:
        if q == ' ':
            word_counter +=1
    print('Count = '+ str(word_counter))        
