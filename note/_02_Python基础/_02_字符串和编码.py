

# Python的字符串

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')

"""
由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
Python对bytes类型的数据用带b前缀的单引号或双引号表示：
"""
x = b'ABC'
print(x)

#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# erro print('中文'.encode('ascii'))

print('ABC'.encode('UTF-8') , len('ABC'.encode('UTF-8')))
print('ABC'.encode('ascii'), len('ABC'.encode('ascii')))
print(b'ABC'.decode('ascii'))
print(b'ABC'.decode('UTF-8'))

"""
如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
要把bytes变为str，就需要用decode()方法：
"""
print(b'ABC'.decode('ascii'))
print( b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 要计算str包含多少个字符，可以用len()函数：
print(len('ABC'))
print(len('中文'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

"""
由于Python源代码也是一个文本文件，
所以，当你的源代码中包含中文的时候，
在保存源代码时，就需要务必指定保存为UTF-8编码。
当Python解释器读取源代码时，为了让它按UTF-8编码读取，
我们通常在文件开头写上这两行：
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：
"""


# 格式化 %运算符用来格式化字符串
"""
在字符串内部，
%s表示用字符串替换，
%d表示用整数替换，
有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
如果只有一个%?，括号可以省略
"""
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

"""
占位符  替换内容
%d      整数
%f      浮点数
%s      字符串
%x      十六进制整数
"""

# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('hello %0.3f' % 123)
print('hello %x' % 123)

# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('Age: %s. Gender: %s' % (25, True))

# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print('growth rate: %d %%' % 7)


# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))