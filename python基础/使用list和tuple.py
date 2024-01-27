# list
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

L = [1, 2, 3, 4, 5]

print(len(L))

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的：
for index, i in enumerate(L):
    print(L[index])

# 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。

# list是一个可变的有序表，所以，可以往list中追加元素到末尾：

L.append('abc')
print(L)

# 也可以把元素插入到指定的位置，比如索引号为1的位置：
L.insert(1, 'cba')
print(L)

# 要删除list末尾的元素，用pop()方法：
last = L.pop()
print(last)
print(L)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
pop_e = L.pop(1)
print(pop_e)
print(L)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
L[2] = 'ABC'
print(L)

# list元素也可以是另一个list
L[3] = ['a', 'b', 'c']
print(L)

L.append(['A', 'B', 'C'])
print(L)

L += ['E', 'F', 'G']
print(L)

L += [['E', 'F', 'G']]
print(L)

L.append([['H', 'I', 'J']])
print(L)

p = ['x', 'y', 'z']
L.insert(4, p)
print(L)

L1 = [1, 2, 3, 4, p, 5]
print(L1)

# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
L2 = []
print(len(L2))

# tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
T = (1, 2, 3, 4, 5)
print(T)
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
T = (1, 2, 3, 4, L1)
print(T)

L1 = [1, 2, 3]
print(T)
T[4][2] = 'a'
print(T)
# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，
# 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
# 理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。


# 但是，要定义一个只有1个元素的tuple，如果你这么定义：t = (1)
# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
t = (1,)
print(t)
# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。

# 练习
# 请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
'''
小结
list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
'''
