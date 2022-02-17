n = int(input())
for i in range(n):
    x = input()
    output = ""
    for q in x:
        output = output + str(ord(q)-64)
    print(output)    