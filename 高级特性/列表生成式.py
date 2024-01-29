# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做
L = [x*x for x in range(1,11)]
print(L)

L = [f'{x}*{x}' for x in range(1,11)]
print(L)

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

L = [f'{x}*{x}' for x in range(1,11) if x%2==0]
print(L)

# 还可以使用两层循环，可以生成全排列：
L = [m+n for m in 'ABC' for n in 'XYZ']
print(L)
# 三层和三层以上的循环就很少用到了。

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os
dirs = [x for x in os.listdir('../')]
print(dirs)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
L = [k+'-->'+v for k,v in d.items()]
print(L)

# 把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
L = [word.lower() for word in L]
print(L)

#if...else...
L = [f'{x}*{x}' for x in range(1,11) if x%2==0]
# 我们不能在最后的if加上else：
# L = [f'{x}*{x}' for x in range(1,11) if x%2==0 else 0] #invalid syntax
# 另一些童鞋发现把if写在for前面必须加else，否则报错：
L = [x*x if x%2 ==0 else x for x in range(1,11)]
print(L)
# 这是因为for前面的部分是一个表达式，它必须根据x计算出一个结果。因此，考察表达式：x if x % 2 == 0，它无法根据x计算出结果，因为缺少else，必须加上else
# 可见，在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。

# 练习
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
# 使用内建的isinstance函数可以判断一个变量是不是字符串：
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [word.lower() for word in L1 if isinstance(word,str)]
print(L2)

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

'''
小结
运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
'''