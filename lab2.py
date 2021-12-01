n = int(input('請輸入數字:'))
a = 2
for i in range(2,n+1):
    while a <= i:
        if i % a == 0:
            break
        elif i % a != 0:
            a = a + 1
    if a != i:
        a = 2
        continue
    elif a == i:
        a = 2
        print(i)