
# 要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：
#
# http://docs.python.org/3/library/functions.html#abs
print(abs(10))
print(abs(-10))

# 而max函数max()可以接收任意多个参数，并返回最大的那个：
print(max(range(1000)))
print(max(list(range(1000))))

print(max(set(range(1000))))

#数据类型转换
# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
print(int('1'))
print(int(12.34))

print(float(1))
print(float('123'))

print(str(4312432))
print(bool(1))
print(bool(''))
print(bool(0))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-1))

# 练习
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n1 =255
n2 = 1000
print(hex(n1))
print(hex(n2))