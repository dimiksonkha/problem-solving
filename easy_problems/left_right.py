t = int(input())
for i in range(t):
    word = input()
    n = len(word)
    for j in range(n):
        if word[j] == "L" and j!=0:
            word = word.replace(word[j], word[j-1],1)
        elif word[j] == "R" and j!= (n-1):
            word = word.replace(word[j], word[j+1],1)    
    print(word)    
           
