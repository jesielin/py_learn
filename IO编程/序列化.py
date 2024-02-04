
#序列化
import pickle

d = dict(name='bob',age=18,score=100)
# with open('./some/some_test.py','wb') as f:
#     pickle.dump(d,f)

# with open('./some/some_test.py','rb') as f:
#     d = pickle.load(f)
#     print(d)

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

#JSON
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
#
# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
#
#   JSON类型	        Python类型
#   {}	            dict
#   []	            list
#   "string"	    str
#   1234.56	        int或float
#   true/false	    True/False
#   null	        None
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：

import json
d = dict(name='bob',age=18,score=100)
# with open('some/some_test1.py','a',encoding='utf-8') as f:
#     json.dump(d,f)

with open('some/some_test1.py','r',encoding='utf-8') as f:
    d = json.loads(f.readline())
    # d1 = json.loads(str(d))
    # print(type(d1))
    s = str(d)
    print(s)
    d1 = json.loads(s.replace('\'','\"')) #json要求字符串用双引号


class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score


s = Student('bob',20,97)
# with open('some/some_test1.py',encoding='utf-8') as f:
#     json.dump(s,f)

def stu2dict(stu):
    return {
        'name':stu.name,
        'age':stu.age,
        'score':stu.score
    }
print(s.__dict__)

# with open('some/some_test1.py','a',encoding='utf-8') as f:
#     # json.dump(s,f,default=stu2dict)
#     json.dump(s,f,default=lambda x:x.__dict__)

def dict2stu(dict):
    return Student(dict['name'],dict['age'],dict['score'])

with open('some/some_test1.py','r',encoding='utf-8') as f:
    d = json.loads(f.readline(),object_hook=dict2stu)
    print(d)

# 练习
# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
o = json.loads(s)
print(o)
'''
小结
Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。

json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。
'''