
import os
import shutil

print(os.name)

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# print(os.uname())

# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# 环境变量

print(os.environ)
for k,v in os.environ.items():
    print(k,'==>',v)

# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print('--------------------')
for i in os.environ.get('path').split(';'):
    print(i)

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
print('---------------------')
print(os.path.abspath('..'))
print(os.path.abspath('.'))

print('---------------------')
path = os.path.join('..','some')
print(path)

# os.mkdir(path)
# os.rmdir(path)

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
#
# part-1/part-2
# 而Windows下会返回这样的字符串：
#
# part-1\part-2

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

a,b = os.path.split(path)
print(a,b)

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
exd = os.path.splitext(r'\some\somee\abc.txt')
print(exd)

# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
#
# # 对文件重命名:
# >>> os.rename('test.txt', 'test.py')
# # 删掉文件:
# >>> os.remove('test.py')

# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
#
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
# path = os.path.join('.','some')
# os.mkdir(path)

L1= [os.path.abspath(os.path.join('..',x)) for x in os.listdir('..') if os.path.isdir(os.path.join('..',x) )]
L2 = [os.path.abspath(x) for x in os.listdir('../..') ]

print('0---------------')
print(L1 == L2)

for i in L1:
    print(i)
    # print('isfile:',os.path.isfile(i))
    # print('isdir:',os.path.isdir(i))
# print(os.path.isdir('..\\函数式编程'))

# 要列出所有的.py文件，也只需一行代码：
L3= [x for x in os.listdir('.') if os.path.splitext(x)[1]=='.py']
print('---------------------')
for i in L3:
    print(i)

'''
小结
Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。
'''
def decode_permissions(permissions):
    # 权限字典，键为八进制数，值为对应的权限字符
    perm_dict = {4: 'r', 2: 'w', 1: 'x'}

    # 检查结果是否为合法的权限数字（0-777）
    if 0 <= permissions <= 0o777:
        # 将数字转换为八进制字符串，然后去掉前两位（'0o'）
        oct_str = oct(permissions)[2:]

        # 确保是三个数字，不足前面补0
        oct_str = oct_str.zfill(3)

        # 解码每个数字对应的权限字符
        decoded_perms = ''
        for digit in oct_str:
            digit_int = int(digit)
            for key, value in perm_dict.items():
                if digit_int >= key:
                    decoded_perms += value
                    digit_int -= key
                else:
                    decoded_perms +='-'
                    # 如果digit_int不为0，说明输入的permissions不合法
            if digit_int != 0:
                return "Invalid permissions"

                # 格式化输出为rwxrwxrwx的形式
        # print('--',decoded_perms)
        return decoded_perms[0:3] + decoded_perms[3:6] +  decoded_perms[6:9]
    else:
        return "Permissions out of range"
# 练习
# 利用os模块编写一个能实现dir -l输出的程序。
import stat
import time
def _dir(path,command='l'):
    files = [x for x in os.listdir(path)]
    for i in files:
        l = []
        st = os.stat(os.path.join(path,i))
        # print(decode_permissions(stat.S_IMODE(st.st_mode)))#权限
        # print(f'{i},{stat.S_ISDIR(st.st_mode)}')
        # print(st)
        # l.append(('d' if stat.S_ISDIR(st.st_mode) else '-') + decode_permissions(stat.S_IMODE(st.st_mode)))
        # l.append(st.st_nlink)
        l.append(time.strftime('%Y/%m/%d %H:%M',time.localtime(st.st_mtime)))
        l.append('<DIR>' if stat.S_ISDIR(st.st_mode) else ' ')
        l.append(str(st.st_size) if not stat.S_ISDIR(st.st_mode) else ' ')
        l.append(i)
        print('\t\t'.join(l))
    return files


# 假设我们有一个二维数组
matrix = [
    [1, 22, 333],
    [44, 5, 66],
    [7, 888, 99]
]

# 找出每一列的最大宽度，以便对齐
col_widths = [max(len(str(row[i])) for row in matrix) for i in range(len(matrix[0]))]

# 使用format()方法和制表符'\t'来打印数组
for row in matrix:
    # 使用zip将每一列的值与其对应的宽度配对，并使用format进行格式化
    formatted_row = ['{:<{}}'.format(str(elem), width) for elem, width in zip(row, col_widths)]
    print('\t'.join(formatted_row))


if __name__ == '__main__':
    print('===================')
    print(_dir('..'))
    print('501:',decode_permissions(0o501))