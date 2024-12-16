# branch and loop structures

"""
status_code = int(input('响应状态码：'))

match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case _:   description = 'Unknown Status Code'

print('状态码描述：', description)
"""
"""
for i in range(1, 9+1):
    for j in range(1, i+1):
        print(f'{i} * {j} = {i*j}', end='\t')     # 这里的目的是不要换行
    print()
"""

"""
a = int(input("Please input the first number: "))
b = int(input("Please input the second number: "))
c = min(a, b)
i = 1
d = 1
while i <= c:
    if 0 == a % i and 0 == b % i:
        d = i
    i += 1

print(f'{a}和{b}的最大公约数是{d}')
"""

"""
# 这里用了辗转相除法
x = int(input('x = '))
y = int(input('y = '))
while x % y != 0:
    x, y = y, x % y
print(f'最大公约数是{y}')
"""
import random
answer = random.randrange(1, 100)
count = 1
while  True:
    num = int(input('please input a number: '))
    if num == answer:
        print(f'Congratulation! You have tried {count} times.')
        break
    count += 1
    if num < answer:
        print('the number is small')
    else:
        print('the number is large')
