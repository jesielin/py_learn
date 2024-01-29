
#dict
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
for k in d.keys():
    print(d[k])

# 为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
#
# 第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。
#
# dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
#
# 你可以猜到，这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value。
#
# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：

d['Adam'] = 67
print(d)

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
d['Jack'] = 97
d['Jack'] = 100

print(d)

# 如果key不存在，dict就会报错：
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Jack' in d)
print(d.get('ABC'))
print(d.get('ABC',999))
print(d.get('ABC','key error'))


# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
key = d.pop('Michael')
print(key)
print(d)

# 和list比较，dict有以下几个特点：
#
# 1.查找和插入的速度极快，不会随着key的增加而变慢；
# 2.需要占用大量的内存，内存浪费多。

# 而list相反：
#
# 1.查找和插入的时间随着元素的增加而增加；
# 2.占用空间小，浪费内存很少。

# 所以，dict是用空间来换取时间的一种方法。

# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：

#set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

s = set([1,2,3])

print(s)
# 注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。

# 重复元素在set中自动被过滤：

s = set([2,2,1,2,3,4,5,4,3])
print(s)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(1)
s.add(1)
s.add(6)
s.add(6)
print(s)

# set和dict的唯一区别仅在于没有存储对应的value，
# 但是，set的原理和dict一样，所以，同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
# s.add([1,2,3]) #list无法作为key存入set
# 通过remove(key)方法可以删除元素：
s.remove(4)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1,3,4])
s2 = set([2,3,5])
print(s1 & s2)
print(s1 | s2)

#不可变对象
s = 'ABC'
s.replace('A','a')
print(s)

# 虽然字符串有个replace()方法，也确实变出了'Abc'，但变量a最后仍是'abc'，应该怎么理解呢？
# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
a = 'ABC'
s = set([*a,'b','c'])
s = set([a,'b','c'])
print(s)
'''
小结
使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。

tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
'''
s = {(1,),'a',(1,2,3)}

print(s)

# s = {(1,),'a',(1,2,3),(1,[1,2])}
# 第四个元素tuple中包含不可哈希的list，所以不能作为key
print(s)