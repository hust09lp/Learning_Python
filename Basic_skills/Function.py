import random
import string

# def fac(num):
#     result = 1
#     for i in range(1, num+1):
#         result *= i
#     return result
#
# print(fac(5))

# def foo():
#     print('Hello World!')
#
# def foo():
#     print('Good Bye!')
#
# foo()

# ALL_CHARS = string.digits + string.ascii_letters
# def ver_code(length = 4):
#     return random.choices(ALL_CHARS, k=length)
#
# print(''.join(ver_code(10)))

# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#         elif i == num - 1:
#             return True
#
# print(is_prime(34))

# def divide(a, b):
#     quotient = a // b
#     remainder = a % b
#     return quotient, remainder
# print(divide(10, 3))

def lcm(x, y):
    return x * y // gcd(x, y)

def gcd(x, y):
    while x % y != 0:
        x, y = y, x % y
    return y
num1 = int(input('please input a number: '))
num2 = int(input('please input another number: '))
print(lcm(num1, num2))