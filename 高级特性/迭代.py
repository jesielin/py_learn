#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

#Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。

#list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，
# 但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

dict = {'b':'a','b':'b','c':'c'}

for key in dict:
    print(key)

print(dict)