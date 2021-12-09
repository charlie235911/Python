def function(user,ans):
    if user == '石頭' and ans == '布':
        print('輸了\n')
        return '輸了'
    elif user == '布' and ans == '剪刀':
        print('輸了\n')
        return '輸了'
    elif user == '剪刀' and ans == '石頭':
        print('輸了\n')
        return '輸了'
    elif user == '石頭' and ans == '石頭':
        print('平手\n')
        return '平手'
    elif user == '布' and ans == '布':
        print('平手\n')
        return '平手'
    elif user == '剪刀' and ans == '剪刀':
        print('平手\n') 
        return '平手'
    elif user == '石頭' and ans == '剪刀':
        print('贏了\n')
        result = '贏了'
        return result
    elif user == '布' and ans == '石頭':
        print('贏了\n')
        return '贏了'
    elif user == '剪刀' and ans == '布':
        print('贏了\n')
        return '贏了'

result = '輸了'
while result != '贏了':
    import random
    list = ['石頭','剪刀','布']
    user = input('出拳: ')
    ans = random.choice(list)
    print('電腦:',ans)
    result = function(user,ans)