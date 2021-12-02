n = int(input('請輸入數字:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        if j == 1:
            continue
        elif i % j == 0:
           break
    if i == 1:
        continue
    elif j == i:
        print(i, end=' ')