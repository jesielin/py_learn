
#统计python代码行数

import os



def count_py_lines(path):
    print('------------count---------------')
    return _count_py_lines(path,'')

def _count_py_lines(path,name):

    print('path:',path)
    # print('path:',path)
    # sum = 0
    # path = os.path.join(path,name)
    # for i in os.listdir(path):
    #     if i in ('.git','.idea'):
    #         continue
    #     if os.path.isfile(os.path.join(path,i)) and os.path.splitext(i)[1]=='.py' :
    #         print('----',i,'is file.')
    #         with open(os.path.join(path,i),'r',encoding='utf-8') as f:
    #             lines = len(f.readlines())
    #         sum = sum + lines
    #     elif os.path.isdir(os.path.join(path,i)):
    #         print('--',i,'is dir.')
    #         sum = sum + _count_py_lines(path,i)
    # return sum
    sum = 0
    for root,dirs,files in os.walk(path):
        print('----------------')
        # for i in dirs:
        #     print('dirs:',i)

        for i in files:
            if i.endswith('.py'):
                print(os.path.join(root,i))
                sum = sum + count_file(os.path.join(root,i))

        # print(root)

        print('----------------')
    return sum


def count_file(path):
    s = 0
    with open(path,encoding='utf-8') as f:
        s = sum(1 for _ in f)
    return s

if __name__ == '__main__':
    sum = count_py_lines('.')

    print(f'一共：{sum}行python代码。')