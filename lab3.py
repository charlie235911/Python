import random
list = ['石頭','剪刀','布']
ans = random.choice(list)
user = input('猜拳:')
if user == '石頭' and ans == '布':
    print('輸了')
elif user == '布' and ans == '剪刀':
    print('輸了')
elif user == '剪刀' and ans == '石頭':
    print('輸了')
elif user == '石頭' and ans == '石頭':
    print('平手')
elif user == '布' and ans == '布':
    print('平手')
elif user == '剪刀' and ans == '剪刀':
    print('平手')
elif user == '石頭' and ans == '剪刀':
    print('贏了')
elif user == '布' and ans == '石頭':
    print('贏了')
elif user == '剪刀' and ans == '布':
    print('贏了')