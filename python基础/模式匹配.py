score = 'B'

match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: # _表示匹配到其他任何情况
        print('score is ???.')

x = (1, 2, 3)

# 使用match关键字匹配元组
match x:
    case (1, 2, y):
        print(f"y is {y}")
    case _:
        print("Not matched")

        # 使用match关键字匹配字典
d = {'a': 1, 'b': 2}

match d:
    case {'a': x, 'b': y}:
        print(f"x is {x}, y is {y}")
    case _:
        print("Not matched")

age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')

# 在上面这个示例中，第一个case x if x < 10表示当age < 10成立时匹配，且赋值给变量x，第二个case 10仅匹配单个值，第三个case 11|12|...|18能匹配多个值，用|分隔。
#
# 可见，match语句的case匹配非常灵活。

args = ['gcc', 'hello.c', 'world.c','a','b','c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ','.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

# 第一个case ['gcc']表示列表仅有'gcc'一个字符串，没有指定文件名，报错；
#
# 第二个case ['gcc', file1, *files]表示列表第一个字符串是'gcc'，第二个字符串绑定到变量file1，后面的任意个字符串绑定到*files（符号*的作用将在函数的参数中讲解），它实际上表示至少指定一个文件；
#
# 第三个case ['clean']表示列表仅有'clean'一个字符串；
#
# 最后一个case _表示其他所有情况。
#
# 可见，match语句的匹配规则非常灵活，可以写出非常简洁的代码。


