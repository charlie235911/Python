n = int(input('請輸入數字:'))
for i in range(2,n+1):
    for j in range(2,i+1):
        if i % j == 0:
            break    
    if j == i:
        print(i, end=' ')