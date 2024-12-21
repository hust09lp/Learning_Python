import math

"""
radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi *radius
area = math.pi * radius ** 2
print(f'{perimeter = :.2f}')
print(f'area = {area:.2f}')
"""

year = int(input("Please input the year: "))
is_leap = 0 == year % 4 and 0 != year % 100 or 0 == year % 400

print(f'The year of {year} is {is_leap}.')


