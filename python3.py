year = int(input('請輸入年分：'))
if year%4==0 and year%100!=0:
    print('閏年')
elif year%100==0 and year%400==0:
    print('閏年')
elif year%100==0 and year%400!=0:
    print('平年')
else:
    print('平年')

guess = 0
answer = 77
while guess!=answer:
    guess = int(input('猜數字：'))
    if guess>answer:
        print('再猜小一點')
    elif guess<answer:
        print('再猜大一點')
print('你猜對了 遊戲結束')

str = 'Python'
list = [5,'abc',6.2]
for i in str:
    print(i)
for i in list:
    print(i)

for i in range(1, 10):
    for j in range(1, 10):
        print(str(i) + '*' + str(j) + '=' + str(i * j), end=" ")
    print('')
    print('')

name = 'Tommy'
age = 19
country = 'Taiwan'
print('My name is %s,%d years old,come from %s'%(name,age,country))
print('My name is {},{} years old,come from {}'.format(name,age,country))
print(f'My name is {name},{age} years old,come from {country}')

