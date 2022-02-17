import sys

def calculate_age(y1,m1,d1,y2,m2,d2):
    y = y1-y2

    if m1 < m2:
        y = y-1
        m1 = m1 +12

    m = m1-m2 

    if d1 < d2:
        m = m-1
        d1 = d1 + 30

    d = d1-d2

    printf("Age is: %d year(s) %d month(s) %d day(s)", y,m,d)

def printf(format, *args):
    sys.stdout.write(format % args)   

calculate_age(2021,2,16,1990,11,22)
