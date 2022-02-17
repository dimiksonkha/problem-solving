vowels ='aieou'
n = int(input())
for i in range(n):
    x = input()
    for q in x:
        if q in vowels:
            print(q,end="")
    
    print()

    for r in x:
        if r not in vowels and r !=" ":
            print(r,end="")
            

