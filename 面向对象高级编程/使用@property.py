# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
class Student():
    pass

s = Student()
s.score = 9999

# 这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
class Student():
    def set_score(self,score):
        if not isinstance(score,int):
            raise ValueError(f'{score} type error')
        elif  score >100 or score<0:
            raise ValueError(f'{score} value error')
        else:
            self.score = score
    def get_score(self):
        return self.score

# 现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：
s = Student()
s.set_score(100)
print(s.get_score())

# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
#
# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！
#
# 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student():
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError(f'{score} type error')
        elif  score >100 or score<0:
            raise ValueError(f'{score} value error')
        else:
            self._score = score
# @property的实现比较复杂，我们先考察如何使用。
# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
# 于是，我们就拥有一个可控的属性操作：

s = Student()
s.score = 60
print(s.score)
# s.score = 999

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
#
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student():
    @property
    def get_birth(self):
        return self._get_birth
    @get_birth.setter
    def get_birth(self,birth):
        self._get_birth = birth
    @property
    def age(self):
        return 2024-self._get_birth

# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
s = Student()
s.get_birth = 100
print(s.age)

#这里的实现与上面的意义相同
class Student():
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2024-self._birth

s = Student()
s.birth = 100
print(s.age)



# 要特别注意：属性的方法名不要和实例变量重名。例如，以下的代码是错误的：
# class Student():
#     @property
#     def birth(self):
#         return self.birth
# 这是因为调用s.birth时，首先转换为方法调用，在执行return self.birth时，又视为访问self的属性，于是又转换为方法调用，造成无限递归，最终导致栈溢出报错RecursionError。

# 小结
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')