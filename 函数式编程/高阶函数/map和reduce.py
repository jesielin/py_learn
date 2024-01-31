import math
from collections.abc import Iterable, Iterator
from functools import reduce

'''
函数式编程
函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。

而函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。

我们首先要搞明白计算机（Computer）和计算（Compute）的概念。

在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。

而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。

对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。

函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
'''

'''
高阶函数英文叫Higher-order function

'''

# 变量可以指向函数
x = abs
print(abs(-10))


# 函数名也是变量
# 那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
#
# 如果把abs指向其他对象，会有什么情况发生？
# abs = 10
# print(abs(-10))

# 把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！
# 当然实际代码绝对不能这么写，这里是为了说明函数名也是变量。要恢复abs函数，请重启Python交互环境。
# 注：由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。

# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))

'''
小结
把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
'''


# map
# 我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
#
# 举例说明，比如我们有一个函数f(x)=x**2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
def f(x):
    return x * x


result = map(f, list(range(1, 11)))
print(list(result))
for i in result:
    print(i)
print(result)
print(isinstance(result, Iterable))  # True
print(isinstance(result, Iterator))  # True

print(list(result))

# map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x**2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
result = map(str, range(1, 11))
print(list(result))


# reduce
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 比方说对一个序列求和，就可以用reduce实现：
def add(x, y):
    return x + y


def sum1(*args):
    s = 0
    print(args)
    for i in args:
        s += i

    return s


result = reduce(sum1, [1, 2, 3, 4, 5])
print(result)
print(isinstance(result, Iterable))  # False
print(isinstance(result, Iterator))  # False


def f(*args, **kw):
    print(args)
    print(kw)


f(1, 2, 3, 4, 5)

# 当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。
#
# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
result = reduce(lambda x, y: 10 * x + y, [1, 3, 5, 7, 9])
print(result)

# 这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
result = reduce(lambda x, y: x + y, '13579')
print(result)

result = reduce(lambda x, y: 10 * x + y, map(lambda x: int(x), '13579'))
print(result)


# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper() + name[1:].lower()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    # print(args)
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    if s[0] == '-':
        sy = -1
        L = s[1:].split('.')
    else:
        sy = 1
        L = s.split('.')
    integer_part = L[0]
    integer_part = reduce(lambda x, y: 10 * x + y, map(lambda x: int(x), integer_part))
    if len(L) == 1:
        float_part = 0
    else:
        float_part = L[1]
        lens = len(float_part)
        float_part = reduce(lambda x, y: 10 * x + y, map(lambda x: int(x), float_part))
        float_part = float_part * (0.1 ** lens)
    return sy*(integer_part + float_part)

# print(str2float('-123.456'))
str2float('123.456')
str2float('123')
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
