

# 字符串

# 转义字符 \  \n换行 \t制表符

print('I\'m ok.')
print('I\'m learning\nPython.')
print('\\\n\\')
print('\\\t\\')

print('''line1
line2
line3''')

print(r'''hello,\n
world''')
# r'''\n''' ->直接输出 \n

print('==========================================================')

# 布尔值 True、False表示布尔值（请注意大小写）

# and运算是与运算，只有所有都为True，and运算结果才是True：
print(True)
print(False)
print(3 > 2)
print(3 > 5)
print(True and True)
print(True and False)
print(False and False)
print(5 > 3 and 3 > 1)

# or运算是或运算，只要其中有一个为True，or运算结果就是True：
print(True or True)
print(True or False)
print(False or False)
print(5 > 3 or 1 > 3)

# not运算是非运算，它是一个单目运算符，把True变成False，False变成True：
print(not True)
print(not False)
print(not 1 > 2)

print('==========================================================')

# 空值 None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
print(None)

print('==========================================================')

# 变量

# 等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

a = 'ABC'
"""
Python解释器干了两件事情：
    1 在内存中创建了一个'ABC'的字符串；
    2 在内存中创建了一个名为a的变量，并把它指向'ABC'。
"""
a = 'ABC'
b = a
a = 'XYZ'
print(b)

print('==========================================================')

# 常量 用全部大写的变量名表示常量

PI = 3.14159265359

# 在Python中，有两种除法，一种除法是/
print(10 / 3) # 3.3333333333333335
print(9 / 3) # 3.0
# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：

# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数：
print(10 // 3)

# 因为//除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：
print(10 % 3)


