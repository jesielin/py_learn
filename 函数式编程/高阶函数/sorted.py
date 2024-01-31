#排序算法

# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？
# 直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

# Python内置的sorted()函数就可以对list进行排序：
print(sorted([4,5,1,4,6,7,8,9]))
print(sorted((4,5,1,4,6,7,8,9)))

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([-1,1,-2,9,-7,12],key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True))

#小结
# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
# 练习
# 假设我们用一组tuple表示学生名字和成绩：
#
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：

def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

# 再按成绩从高到低排序：
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score,reverse=True)
print(L2)