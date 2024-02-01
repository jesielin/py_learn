# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
import types

print(type('123'))  # <class 'str'>
print(type(123))  # <class 'int'>
print(type(None))  # <class 'NoneType'>
print(type(abs))  # <class 'builtin_function_or_method'>
print(type(int))  # <class 'type'>


class Animal():
    pass


a = Animal()
print(type(a))  # <class '__main__.Animal'>
print(type(Animal))  # <class 'type'>
import os

print(type(os))  # <class 'module'>
import 访问限制

s = 访问限制.Student('b', 1)
print(type(s))  # <class '访问限制.Student'>


def t():
    pass


print(type(t))  # <class 'function'>

# 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
#
# >>> type(123)==type(456)
# True
# >>> type(123)==int
# True
# >>> type('abc')==type('123')
# True
# >>> type('abc')==str
# True
# >>> type('abc')==type(123)
# False
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
print('-----------------')
print(type(os) == types.ModuleType)  # True
print(type(abs) == types.BuiltinMethodType)  # True
print(type('123') == str)  # True
print(type(s) == 访问限制.Student)  # True
print(type(lambda x: x) == types.LambdaType)  # True
print(type((x for x in range(10))) == types.GeneratorType)  # True

# 使用isinstance()
print('-----------------')
print(isinstance(os, types.ModuleType))  # True
print(isinstance(abs, types.BuiltinMethodType))  # True
print(isinstance('123', str))  # True
print(isinstance(s, 访问限制.Student))  # True
print(isinstance(lambda x: x, types.LambdaType))  # True
print(isinstance((x for x in range(10)), types.GeneratorType))  # True
# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple)))  # True
print(isinstance((1, 2, 3), (list, tuple)))  # True
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir(str))
print(dir(访问限制.Student))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print('ABC'.__len__())
print(len('ABC'))

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
print(hasattr(str,'__len__'))#True
s1 =访问限制.Student('bob',97)
print(hasattr(s1,'get_gender')) #True
print(hasattr(s1,'some')) #True
print(getattr(s1,'some'))
setattr(s1,'some',2)
print(getattr(s1,'some'))

print(getattr(s1,'_Student__gender'))
setattr(s1,'_Student__gender',2)
print(getattr(s1,'_Student__gender'))

# 如果试图获取不存在的属性，会抛出AttributeError的错误：
# 可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(s1,'__gender',404))

# 也可以获得对象的方法：
print(hasattr(s1,'set_gender'))#True
fn = getattr(s1,'set_gender')
print(fn)
print(s1.get_gender())
fn('male')
print(s1.get_gender())
'''
小结
通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：

sum = obj.x + obj.y
就不要写：

sum = getattr(obj, 'x') + getattr(obj, 'y')
一个正确的用法的例子如下：

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
'''
