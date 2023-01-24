import math
a = int (input('a ='))
c = int(input('c = '))

chuise = int(input('k(1) OR b(2):'))
if chuise == 2:
    b = int(input('Enter b: '))
    dis = b**2-4*a*c
    print('dis = ', dis)
    if dis > 0:
        asd = math.sqrt(dis)
        x1 = (-b+asd)/2*a
        #*************************
        x2 = (-b-asd)/2*a
        print('x1 = ', x1)
        print('x2 = ', x2)
    elif dis == 0:
        x = (-b)/2*a
        print('x = ',x)
    else:
        print('BRUH MOMENT')
else:
    k = int(input('Enter k: '))
    dis = k**2-a*c
    print('dis = ', dis)
    if dis > 0:
        asd = math.sqrt(dis)
        x1 = (-k + asd) / a
        # *************************
        x2 = (-k - asd) / a
        print('x1 = ', x1)
        print('x2 = ', x2)
    elif dis == 0:
        x = (-k) / a
        print('x = ', x)


