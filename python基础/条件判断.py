# 条件判断
# 计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。

# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

# 也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了：
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

# 当然上面的判断是很粗略的，完全可以用elif做更细致的判断：

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# elif是else
# if的缩写，完全可以有多个elif，所以if语句的完整形式就是：

# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

# if判断条件还可以简写，比如写：
if "":
    print('True')

if []:
    print('True')

if 0:
    print('True')

if "1":
    print('True')

if [1]:
    print('True')

if 1:
    print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。


# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：

# s = input('birth: ')
birth = int('2012')
if birth < 2000:
    print('00前')
else:
    print('00后')

# 练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：
import math
height = 1.7
weight = 70
bmi = weight / math.pow(height, 2)
if bmi < 18.5:
    print('过轻')
elif bmi >= 18.5 and bmi < 25:
    print('正常')
elif bmi >= 25 and bmi < 28:
    print('过重')
elif bmi >= 28 and bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
