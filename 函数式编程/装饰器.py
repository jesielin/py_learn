import time


# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。

# 函数对象有一个__name__属性（注意：是前后各两个下划线），可以拿到函数的名字：

def now():
    print('2024')
f = now
f()
print(f.__name__)
print(f.__qualname__)

f = lambda x,y:x+y
print(f.__name__)
print(f.__qualname__)

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

def log(func):
    def wrapper(*args,**kw):
        print('call %s:' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2024-1-31')

# now()
# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)
now()
print(now.__name__)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
#
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log(text):
    t = 1
    def decorator(func):

        def wrapper(*args, **kw):
            nonlocal t
            t= t+1
            print('%d %s %s():' % (t+1,text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
print('---------------------')
@log('exec')
def now():
    print('2024-1-31')
now()

# 我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
# 相当于log('exec')(now)
print(now.__name__)

# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
#
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2024-1-31')
print('-----------------')
print(now.__name__)
now()
# 或者针对带参数的decorator：
def log(text):

    def decortator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('call %s %s():' % (text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decortator

@log('exec')
def now():
    print('2014-1-31')

print('--------------')
print(now.__name__)
now()

# 练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        print('calling %s()',func.__name__)
        result = func(*args,**kwargs)
        end = time.time()
        print(f'运行了{end-start}秒')
        return result
    return wrapper
@metric
def anyy():
    time.sleep(2)
    print('aaaaaaaaaa')

print('-----------------')
print(anyy.__name__)
# anyy()

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功！')

'''
在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。

请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

再思考一下能否写出一个@log的decorator，使它既支持：
@log
def f():
    pass
    
又支持：

@log('execute')
def f():
    pass
    
'''

from typing import Any,Callable
def log(f_or_a):
    if isinstance(f_or_a,str):

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kwargs):
                print('%s begin call' % f_or_a)
                result = func(*args,**kwargs)
                print('end call')
                return result
            return wrapper
        return decorator
    else:
        @functools.wraps(f_or_a)
        def wrapper(*args, **kwargs):
            print('begin call')

            result = f_or_a(*args, **kwargs)
            print('end call')
            return result

        return wrapper


@log
def now():
    print('2024-1-31')

print('-----------------')
print(now.__name__)
now()
@log('exec')
def now1():
    print('2024-1-31')
print('------------------')
print(now1.__name__)
now1()
