import time
import sys

# 能清除之前打印内容的输出
def clear_print():
    sys.stdout.write('\r')
    sys.stdout.flush()

#  创建学生对象
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        print(f'{self.name}正在玩游戏.')

# 创建对象
stu1 = Student('张三', 15)
stu2 = Student('李四', 20)
# print(stu1)
# print(stu2)
# print(hex(id(stu1)), hex(id(stu2)))

# 调用对象的方法
Student.study(stu1, 'Python程序设计')
stu1.study('Java程序设计')

# 创建时钟对象
class Clock:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second += 1
        if self.second >= 60:
            self.minute += 1
            self.second = 0
            if self.minute >= 60:
                self.hour += 1
                self.minute = 0
                if self.hour >= 24:
                    self.hour = 0

    def show(self):
        print(f'\r{self.hour} : {self.minute} : {self.second}', end='')

clk1 = Clock(23, 48, 58)

# for _ in range(20):
#     clk1.show()
#     time.sleep(1)
#     clk1.run()
