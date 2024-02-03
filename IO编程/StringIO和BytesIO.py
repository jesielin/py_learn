
# StringIO
# 很多时候，数据读写不一定是文件，也可以在内存中读写。
#
# StringIO顾名思义就是在内存中读写str。
#
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：

from io import StringIO,BytesIO
import io

f = StringIO()

f.write('123')
f.write('456')
f.write('789')
# print(f.getvalue())
# getvalue()方法用于获得写入后的str。
#
# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：

f = StringIO('XXYYZZ',newline='\n')
print(f.tell())
f.seek(4)
# f.seek(-2,1)
f.write('123')
f.write('456\n')
f.write('789')
f.seek(0)
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s,end='')

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.tell())
f.seek(-6,io.SEEK_END) #只有字节流可以seek负数
print(f.tell())
print(f.read())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())


'''
小结
StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
'''