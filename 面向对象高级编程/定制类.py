
#定制类
# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
#
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
#
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。
#
# __str__

class Student():
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def __str__(self):
        return f'{self.__name}的分数是{self.__score}'



s = Student('bob',97)
print(s)
# 但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：
#
# >>> s = Student('Michael')
# >>> s
# <__main__.Student object at 0x109afb310>
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
#
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：

class Student():
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def __str__(self):
        return f'{self.__name}的分数是{self.__score}'

    __repr__ = __str__


s = Student('shawn',100)
print(s)

# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
#
# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：

class Fib():
    def __init__(self):
        self.__a,self.__b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.__a,self.__b = self.__b,self.__a+self.__b
        if self.__a >10000:
            raise StopIteration()
        return self.__a

f = Fib()
for i in f:
    print(i,end=' ')

print('-------')
print(f)
print(list(f))

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
#
# >>> Fib()[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'Fib' object does not support indexing
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib():
    def __init__(self):
        self.__a,self.__b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.__a,self.__b = self.__b,self.__a+self.__b
        if self.__a >10000:
            raise StopIteration()
        return self.__a
    def __getitem__(self, item):
        i,a,b = 0,1,1
        for i in range(item):
            a,b = b,a+b
        return a


f = Fib()
print(f[5])

# 但是list有个神奇的切片方法：
#
# >>> list(range(100))[5:10]
# [5, 6, 7, 8, 9]
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib():
    def __init__(self):
        self.__a,self.__b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.__a,self.__b = self.__b,self.__a+self.__b
        if self.__a >10000:
            raise StopIteration()
        return self.__a
    def __getitem__(self, item):
        if isinstance(item,slice):
            print(item,'is slice')
            print(item.start)
            print(item.step)
            print(item.stop)
            start = item.start if item.start else 0

            i,a,b = 0,1,1
            for i in range(start):
                a,b = b,a+b
            i = start
            L = []
            for i in range(item.stop):
                L.append(a)
                a,b = b,a+b
            return L


        elif isinstance(item,int):
            i,a,b = 0,1,1
            for i in range(item):
                a,b = b,a+b
            return a

f = Fib()
print(f[2:10])
# 但是没有对step参数作处理：
#
# >>> f[:10:2]
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
#
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
#
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
#
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
# class Student(object):
#
#     def __init__(self):
#         self.name = 'Michael'
# 调用name属性，没问题，但是，调用不存在的score属性，就有问题了：
#
# >>> s = Student()
# >>> print(s.name)
# Michael
# >>> print(s.score)
# Traceback (most recent call last):
#   ...
# AttributeError: 'Student' object has no attribute 'score'
# 错误信息很清楚地告诉我们，没有找到score这个attribute。
#
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':
            return lambda :100
        raise AttributeError('\'Student\' object has no attribute \'%s\''%item)

s = Student()
print(s.name)
# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
print(s.score)
# 返回函数也是完全可以的：
print(s.age())
# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
# print(s.birth)#AttributeError: 'Student' object has no attribute 'birth'

class Chain():
    def __init__(self,path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s ' % (self._path,item))
    def __str__(self):
        return self._path

    __repr__ = __str__

c = Chain()
print(c)
print(c.status.user.timeline.list)

# 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
#
# 还有些REST API会把参数放到URL中，比如GitHub的API：
#
# GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：
#
# Chain().users('michael').repos
# 就可以非常方便地调用API了。有兴趣的童鞋可以试试写出来。
class Chain():
    def __init__(self,path=''):
        self._path = path

    def __getattr__(self, item):
        if item == 'users':
            return lambda x:Chain('%s/users/:%s' % (self._path,x))
        else:
            return Chain('%s/%s' % (self._path,item))
    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().users('michael').repos)

# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
#
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('bob')
s()
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
#
# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
#
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：

print(callable(s))#True
print(callable(abs))#True
print(callable([1,2,3]))#False
print(callable('123'))#False
print(callable(None))#False
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

'''
小结
Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。

本节介绍的是最常用的几个定制方法，还有很多可定制的方法，请参考Python的官方文档。
https://docs.python.org/3/reference/datamodel.html#special-method-names
'''

