# Python内建的filter()函数用于过滤序列。
#
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
from collections.abc import Iterable,Iterator
result = filter(lambda x:x%2==0 ,range(1,11))
print(result)
print(isinstance(result,Iterable)) #True
print(isinstance(result,Iterator))#True

print(list(result))
# 把一个序列中的空字符串删掉，可以这么写：
result = filter(lambda x:x != '' ,['','A','','B'])
print(list(result))

# 可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

'''
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

首先，列出从2开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

不断筛下去，就可以得到所有的素数。

用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
'''

def _odd_iter():
    n = 2
    while True:
        yield n
        n = n+1
def _not_visible(n):
    return lambda x:x%n != 0
def odd():
    iter = _odd_iter()

    while True:
        a = next(iter)
        yield a
        iter = filter(_not_visible(a),iter)

o = odd()
i = 0
while True:
    if i > 100:
        break
    i +=1
    print(next(o))

# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(x):
    s = str(x)
    if len(s) == 1:
        return True
    elif len(s) %2 != 0:
        half = len(s)//2
        s = s[:half] + s[half+1:]
    left = s[:len(s)//2]
    right = s[::-1][:len(s)//2] #字符串翻转
    if left == right:
        return True
    else:
        return False

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

'''
小结
filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
'''