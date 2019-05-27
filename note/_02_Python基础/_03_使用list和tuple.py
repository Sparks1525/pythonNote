
# list
# 列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

classmates =  ['Michael', 'Bob', 'Tracy']
print(classmates, len(classmates))
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的：
print(classmates[0])

# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Adam')

# 也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1,'Jack')

# 要删除list末尾的元素，用pop()方法：
delItem = classmates.pop()
print(delItem)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
delItem = classmates.pop(1)
print(delItem)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah'
print(classmates)

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]

# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

# tuple 一种序列表叫元组 tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')




