n = int(input())
for i in range(n):
    words = input().split()
    for word in words:
        print(word[::-1], end=" ")
    