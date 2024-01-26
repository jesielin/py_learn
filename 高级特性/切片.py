
L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# 取前n个元素,如果第一个index是0，可以省略
print(L[0:3])
print(L[:3])
print(L[1:3])

# -1代表倒数第一个元素的index
print(L[-2:-1])
print(L[-2:])

#前10个数
print(L[:10])
#后10个数
print(L[-10:])
#11-20个数
print(L[10:20])

#前10个数，每两个取一次
print(L[0:10:2])
print(L[:10:2])

#所有数，每5个取一次
print(L[::5])

#tuple也是一种list，唯一区别是tuple不可变，所以tuple也可以切片，只是切片的结果仍然是tuple
t = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

print(t[::5])
print(type(t[::5]))

#字符串也可以看做list，字符串切片之后仍然是字符串
s = '123456789'
print(s[::3])
print(type(s[::3]))

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')