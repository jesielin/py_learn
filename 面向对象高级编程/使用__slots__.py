from types import MethodType
class Student():
    pass

s = Student()

s.name = 'Bob'
print(s.name)
# 还可以尝试给实例绑定一个方法：
def set_age(self,age):
    self.age = age

s.set_age =  MethodType(set_age,s)

s.set_age(11)
print(s.age)
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 =  Student()
# s2.set_age(11) #AttributeError: 'Student' object has no attribute 'set_age'


# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
    self.score = score

Student.set_score = set_score
s2.set_score(100)
s.set_score(99)
print(s2.score)
print(s.score)
# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s1 = Student()
s1.name ='a'
s1.age = 'b'
# s1.score = 98 #AttributeError: 'Student' object has no attribute 'score'

# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

class GraduateStudent(Student):
    pass

s2 = GraduateStudent()

s2.name ='a'
s2.age = 'b'
s2.score = 98
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
class NonGraduateStudent(Student):
    __slots__ = ('score',)
    pass

s3 = NonGraduateStudent()
s3.name ='a'
s3.age = 'b'
s3.score = 98
# s3.gender = 'male' #AttributeError: 'NonGraduateStudent' object has no attribute 'gender'

class Student(object):
    def __init__(self, name):
        self.name = name

class Classmate(Student):
    __slots__ = ('name','age')
    def __init__(self,name):
        self.name =name

B = Classmate('ami')
B.gender = 'female'
print(B.gender)
#父类没有__slot__，子类有__slot__时，子类实例仍可以随意修改变量