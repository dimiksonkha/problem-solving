n = int(input())
vowels = 'aeiou'
for i in range(n):
    sentence = input()
    counter = 0
    for q in sentence:
        if q in vowels:
            counter +=1
    print('Number of vowels = ' + str(counter))        