import random

"""
for num in range(2, 101):
    for div in range(2, num):
        if 0 == num % div:
            break
        elif div == num - 1:
            print(num)
"""

"""
num_new = 1
num_old = 1
print(num_old)
print(num_new)
for i in range(1, 21):
    temp = num_new
    num_new += num_old
    print(num_new)
    num_old = temp
"""
"""
a, b = 0, 1
for _ in range(20):
    a, b = a+b, a
    print(a)
"""
"""
for num in range(100, 1000):
    if num == int(str(num)[0])**3 + int(str(num)[1])**3 + int(str(num)[2])**3:
        print(num)
"""

"""
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
"""

money = 1000
while money > 0:
    print(f'你的总资产为: {money}元')
    # 下注金额必须大于0且小于等于玩家的总资产
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    # 用两个1到6均匀分布的随机数相加模拟摇两颗色子得到的点数
    first_point = random.randrange(1, 7) + random.randrange(1, 7)
    print(f'\n玩家摇出了{first_point}点')
    if first_point == 7 or first_point == 11:
        print('玩家胜!\n')
        money += debt
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print('庄家胜!\n')
        money -= debt
    else:
        # 如果第一次摇色子没有分出胜负，玩家需要重新摇色子
        while True:
            current_point = random.randrange(1, 7) + random.randrange(1, 7)
            print(f'玩家摇出了{current_point}点')
            if current_point == 7:
                print('庄家胜!\n')
                money -= debt
                break
            elif current_point == first_point:
                print('玩家胜!\n')
                money += debt
                break
print('你破产了, 游戏结束!')

