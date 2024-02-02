# 使用枚举类

# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
#
# JAN = 1
# FEB = 2
# MAR = 3
# ...
# NOV = 11
# DEC = 12
# 好处是简单，缺点是类型是int，并且仍然是变量。
#
# 更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：

from enum import Enum, unique

Month = Enum('月份',
             ('一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月',))
print(Month)
print(Month.__members__.items())
for i in Month.__members__:
    print(i)

for name, member in Month.__members__.items():
    print(name, '==>', member, ',', member.value)


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
@unique
class Weekday(Enum):
    周一 = 0  # value为0
    周二 = 1  # value为0
    周三 = 2  # value为0
    周四 = 3  # value为0
    周五 = 4  # value为0
    周六 = 5  # value为0
    周日 = 6  # value为0


# @unique装饰器可以帮助我们检查保证没有重复值。

day1 = Weekday.周一
print(day1 == Weekday['周一'])  # True
print(day1 == Weekday(0))  # True

# print(Weekday(7)) #ValueError: 7 is not a valid Weekday
for name, member in Weekday.__members__.items():
    print(name, '==>', member, ',', member.value)

# 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。

# 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：



class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


'''
小结
Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
'''