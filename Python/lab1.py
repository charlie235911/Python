import sys
a = float(input('請輸入數字:'))
b = float(input('請輸入數字:'))
c = float(input('請輸入數字:'))
d = b**2 - 4*(a*c)
x1 = ((-b) + (b**2 - 4*(a*c))**(1/2))/2*a
x2 = ((-b) - (b**2 - 4*(a*c))**(1/2))/2*a
if (d) < 0:
    print('bx**2 – 4ac是負值有0個實數根')
elif (d) == 0:
    print('bx**2 – 4ac是0有1個重根')
    print(x1)
elif (d) > 0:
    print('bx**2 – 4ac是正值有2個實數根')
    print(x1,x2)