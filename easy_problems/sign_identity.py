n = int(input())
lower_chars = list(range(97,123))
uppper_chars = list(range(65,91))
special_chars = list(range(32,48)) + list(range(58,65)) + list(range(91,97)) + list(range(123, 127))
digits = list(range(48,58))

for i in range(n):
    x = input()
    ascii_value_x = ord(x)
    if ascii_value_x in lower_chars:
        print('Lowercase Character')
    elif ascii_value_x in uppper_chars:
        print('Uppercase Character')
    elif ascii_value_x in special_chars:
        print('Special Character')
    elif ascii_value_x in digits:
        print('Numerical Digit')            