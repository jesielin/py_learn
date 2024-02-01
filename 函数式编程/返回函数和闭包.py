# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
def calc_sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：

def lazy_sum(*args):
    def sum():
        sum = 0
        for i in args:
            sum = sum + i
        return sum
    return sum

print(lazy_sum(1,2,3,4,5))
f= lazy_sum(1,3,5,7,9)

# 调用函数f时，才真正计算求和的结果：
print(f())

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量
# ，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。

# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1,2,3,4,5)
f2 = lazy_sum(1,2,3,4,5)
print(f1==f2)
# f1()和f2()的调用结果互不影响。

#闭包

# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
#
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1()) #9
print(f2()) #9
print(f3()) #9
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。!!!

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(i):
        def g():
            return i*i
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count()
print(f1()) #1
print(f2()) #4
print(f3()) #9
# 缺点是代码较长，可利用lambda函数缩短代码。
def count():
    def f(i):
        return lambda :i*i

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count()
print(f1()) #1
print(f2()) #4
print(f3()) #9

#nonlocal
# 使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常：
# 但是，如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错：
# 原因是x作为局部变量并没有初始化，直接计算x+1是不行的。
# 但我们其实是想引用inc()函数内部的x，
# 所以需要在fn()函数内部加一个nonlocal x的声明。
# 加上这个声明后，解释器把fn()的x看作外层函数的局部变量，它已经被初始化了，可以正确计算x+1。

def inc():
    x = 0
    def f():
        # nonlocal x
        # x = x +1
        return x+1
    return f
f = inc()
print(f())
# 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。！！！

# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    x = 0
    def counter():
        nonlocal x
        x += 1
        return x
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
'''
小结
一个函数可以返回一个计算结果，也可以返回一个函数。

返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
'''