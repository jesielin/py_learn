#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

#Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。

#list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，
# 但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

dict = {'a':'a','b':'b','c':'c'}

for key in dict:
    print(key)

print(dict)

# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
#
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
for v in dict.values():
    print(v)


for k,v in dict.items():
    print(k,v)

# 由于字符串也是可迭代对象，因此，也可以作用于for循环：

for ch in 'ABC':
    print(ch)

# 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
#
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断：

from collections.abc import Iterable
print(isinstance(dict.items(),Iterable))
print(isinstance(dict.keys(),Iterable))
print(isinstance(dict.values(),Iterable))
print(isinstance('ABC',Iterable))
print(isinstance([],Iterable))
print(isinstance((1,),Iterable))

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for index,i in enumerate([1,2,3,4,5]):
    print(index,i)

# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if L is None:
        raise TypeError('None')

    if len(L) == 0:
        return None,None
    x,y = L[0],L[0]
    for i in L:
        x = min(i,x)
        y = max(i,y)
    return x,y
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

'''
小结
任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
'''