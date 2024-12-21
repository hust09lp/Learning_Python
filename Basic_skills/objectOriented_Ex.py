from enum import Enum
import random
from abc import ABCMeta, abstractmethod

class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)

# for suite in Suite:
#     print(f'{suite}: {suite.value}')

class Card:

    def __init__(self, suite, face):
        self.suite = suite
        self.face =face

    # 运算符重载
    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        else:
            return self.suite.value < other.suite.value

    # 这好像是用来做输出打印的函数
    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

# card1 = Card(Suite.SPADE, 6)
# card2 = Card(Suite.DIAMOND, 12)
# print(card1)
# print(card2)

class Poker:

    def __init__(self):
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]
        self.current = 0

    # 把牌洗乱
    def shuffle(self):
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        return self.current < len(self.cards)

# poker = Poker()
# print(poker.cards)
# poker.shuffle()
# print(poker.cards)

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()

poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]

# for _ in range(13):
#     for player in players:
#         player.get_one(poker.deal())
#
# for player in players:
#     print(f'{player.name}:', end=' ')
#     player.arrange()
#     print(player.cards)

# 新建员工类
class Employee(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    # 这里完全就是预留给子类去重写的
    @abstractmethod
    def get_salary(self):
        pass

# 部门经理
class Manager(Employee):

    def get_salary(self):
        return 15000.0

# 程序员
class Programmer(Employee):

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour

# 销售员
class Salesman(Employee):

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05

emps = [Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Programmer('郭嘉'), Salesman('张辽')]
for emp in emps:
    if isinstance(emp, Programmer):
        emp.working_hour = float(input(f'请输入{emp.name}工作小时数：'))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}销售业绩：'))
    print(f'{emp.name}的薪水为{emp.get_salary()}.')
