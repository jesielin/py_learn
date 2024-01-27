import math

# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

# 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：
# 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：
# 所以你看到很多网页的源码上会有类似<meta charset="UTF-8" />的信息，表示该网页正是用的UTF-8编码。


# python中的字符串
# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，例如：

print('带中文的str')

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))
print(ord('中'))
print(chr(65))
print(chr(20013))
# 如果知道字符的整数编码，还可以用十六进制这么写str：
print('\u4e2d\u6587')

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：

print(b'ABC')
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
#
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：


print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
print('012'.encode('utf-8'))
print('\\'.encode('utf-8'))
print('\\'.encode('ascii'))
print('中文'.encode('utf-8'))

# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
#
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xe6\x96'.decode('utf-8', errors='ignore'))

# 要计算str包含多少个字符，可以用len()函数：
print(len('ABC'))
print(len('中文'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('你好啊'.encode('utf-8')))
# 可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
# 在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。

# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：
# 如果.py文件本身使用UTF-8编码，并且也申明了# -*- coding: utf-8 -*-，打开命令提示符测试就可以正常显示中文：

# 格式化
# 在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
# 你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('Hello, %s' % 'world')
# 占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
# 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print('%d \\n%%' % 1)
print('%d \t%%' % 1)

# format()
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# f-string
# 最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：

s1 = 72
s2 = 85

r = (s2 - s1) / s1 * 100
print(f'小明成绩提升了{r:.1f}%')

'''
小结
Python 3的字符串使用Unicode，直接支持多语言。

当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8。Python当然也支持其他编码方式，比如把Unicode编码成GB2312：

>>> '中文'.encode('gb2312')
b'\xd6\xd0\xce\xc4'
但这种方式纯属自找麻烦，如果没有特殊业务要求，请牢记仅使用UTF-8编码。

格式化字符串的时候，可以用Python的交互式环境测试，方便快捷。
'''
