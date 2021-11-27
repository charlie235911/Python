print('hello world')
print(1+2)
print(8+9)

input_date = input('請輸入今天的日期:')
print('今天的日期:')
String1='啦課上次二第'
print(String1[::-1])
input_1 = int(input("請輸入整數:"))
input_2 = int(input("請輸入整數:"))
print(input_1+input_2)
print('整數型態:',type(input_1+input_2))
print(input_1-input_2)
print(input_1*input_2)
print(input_1/input_2)
print(input_1%input_2)
print(input_1//input_2)
print(input_1**input_2)
List1 = [12,24,48,'Python','HackerSir']
print(List1[0])
print(List1[0:2])
print(List1[3][0])
print(List1[4][0:6])


a = int(input('請輸入數字:'))
b = int(input('請輸入數字:'))
if a%b == 0:
    print(str(a)+'可以被'+str(b)+'整除')