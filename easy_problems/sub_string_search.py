n = int(input())

for i in range(n):
    str1, str2 = input().split()
    for j in range (len(str1)):
        if str1[j] == str2[0]:
            sub_string = str1[j:j+len(str2)]
            if sub_string == str2:
                print(j)
                break
            
