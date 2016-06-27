#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#l字符转义
print(' I\' am \"OK\"')
print(r' \\\t\\\ ')
print('''
    line1
    lin32
    line3''')
print('result1:',3 > 2)
print('result2:',3 > 5)
print('/:',10/3,9/3,10//3,9//3,10%3,9%3)

#布尔值运算
print('result3:',3 > 2 and 3 > 5)
print('result4:',3 > 2 or 3 > 5)
print('result5:',not 3 > 2, not 3 > 5)

#字符串和编码
print('包涵中文的字符')
print('字符：',ord('A'), ord('中'),chr(66),chr(25991),'\u4e2d\u6587')

#bytes类型
x = b'ABC'
x2 = b'\xe4\xb8\xad\xe6\x96\x87'

#str类型
y = 'ABC'
z = '中文'

print(x,y)

# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

#encode 将str转为字节bytes
print('1',y.encode('ascii'))
print('2',y.encode('utf-8'))
print('3',z.encode('utf-8'))
#print('4',z.encode('ascii')) #会报错，因为中文编码的范围超过了ASCII编码的范围

#decode 将字节bytes转为str
print('4',x.decode('ascii'))
print('5',x2.decode('utf-8'))

#计算str长度
print('6',len(y),len(z));
#计算bytes字节数
print('7',len(x),len(x2));

#格式化字符
print('格式化字符1 %s %d' % ('asd',100))
print('格式化字符2 %2d %02d' % (2,2))
print('格式化字符3 %.2f' % 3.1415926)
print('格式化字符4 %s  %s' % (3.1415926, True))
print('格式化字符4 %s  %s %%' % (3.1415926, True))#%%转义为%
print('格式化字符5 %d' % 10)

#list和tuple 列表和元组
classmates = ['a', 100, True]
print(classmates)
print(len(classmates))#list元素个数
print(classmates[0])
print(classmates[-1])#最后一个元素
print(classmates[-2])#倒数第二个元素
classmates.append('d')#向list中追加元素
print(classmates)
classmates.insert(0, 'x')#向list中插入元素
print(classmates)
classmates.pop(0)#删除list中的元素
print(classmates)
classmates[0] = 'z'#替换list中的元素
print(classmates)

#list嵌套
s = ['ok', 'not', ['1', '2', '3']]
print(s, len(s))
o = ['p', s, True]
print(o[1][2])

L = []
print(len(L))#空list

#tuple, 不可以增删改
name = ('a', 'b', 'c')
print(name)

name = (1,)
print(name)

name = (1)
print(name)

#tuple和list的嵌套
tu = (1, 2, 3, s)
print(tu[3][2][2])
tu[3][2][2] = 4
print(tu[3][2])

#条件判断
#输入
#name = input('please input your name: ')
#print('hello', name)

#输入+判断
#a = input('inptu a: ')
#b = int(a)

#if b > 5:
#    print('a large',b)
#else:
#    print('a small',-b)

#循环
for a in s:
    print(a)

sum = 0
for x in [1, 2, 3, 4, 5,]:
    sum = sum + x
print(sum)

#range()函数，可以生成一个证书序列
print(list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
#print(n)
print(sum)

#死循环
#while n < 100:
#    n = n - 2
#    print(n)

#使用dict和set
d = {'a':99, 'b':90, 'c':88}
print(d, d['a'])
d['a'] = '100'
print(d['a'])
#print(d['d'])
print('a' in d, 'd' in d)
print(d.get('a'), d.get('d'))
d.pop('c')
print(d)

#和list比较，dict有以下几个特点：

#查找和插入的速度极快，不会随着key的增加而变慢；
#需要占用大量的内存，内存浪费多。
#而list相反：

#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。

#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

#这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

#要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：

a = {'q':12, 'b':True, 'c':[1,2,3]}
print(a)
a = {'q':12, True:'b', 'c':[1,2,3]}
print(a[True])
a = {'q':12, True:'b', 'q':[1,2,3]}
print(a)

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3, 2, 3, 1])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)

x = set([3, 5, 6, 7, 8])
print(x)

print(s & x)
print(s | x)
#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
#s = set([1, [1, 2, 3], 3, 2, 3, 1])
#print(s)

a = ['c', 'b', 'a']
print(a)
a.sort()
print(a)

a = 'abc'
print(a)
a.replace('a', 'A')
print(a.replace('a', 'A'))
print(a)

t = (1,2,3)
d = {'a': s}
s = set(t)
print(d)
print(s)

#t = (1,[2,3])
#d = {'a': s}
#s = set(t)
#print(d)
#print(s)

a = abs(-101)
print(a)

a = max(1, 2)
print(a)

a = int('123')
print(a)

a = str(123)
print(a)

a = float('1.123')
print(a)

a = bool(a)
print(a)

a = bool('')
print(a)

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-101))

n = 255
print(hex(n))

#定义函数－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(-10), my_abs(11))

#空函数 pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass
print(nop)


def mmy_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return-x

print(mmy_abs(1))

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi/6)
print(x, y)
r = move(100, 100, 60, math.pi/6)
print(r)

def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('a is bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError('b is bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('c is bad operand type')
    x = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
    y =  (-b - math.sqrt(b*b - 4*a*c))/(2*a)

    return x, y

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
print(quadratic(1, 3, -4))

#函数的参数－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
#默认参数
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5), power(5, 2), power(5, 3))

def enroll(name, age, city='nanjing', type='ok'):
    print(name, age, city, type)

print(enroll('a', 'b', 'c'))
print(enroll('a', 'b', type='no'))


#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(calc(1,2))
print(calc())

num = [1, 2]
print(calc(*num))

#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(person('kang', 30))
print(person('kang', 30, gender='male', jobs='enginner'))

extra = {'city': 'nanj', 'job':'engineer'}
print(person(1, 2, **extra))

#命名关键字参数-限制关键字参数的名字
def person(name, age, *, city, job):
    print(name, age, city, job)

print(person('aa', 24, city='nanj', job='enginner'))


#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw)
print(f1(1, 2))
print(f1(1, 2, c=3))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, 'a', 'b', x=99))
print(f2(1, 2, d=99, ext=None))

#递归函数－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(1), fact(5), fact(100))

#在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
#print(fact(1000))

#尾递归
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(5))

#http://www.cnblogs.com/yanlingyin/archive/2011/11/14/2247594.html

print('---汉诺塔的递归算法---')

i = 0
def move(n, a, b, c):
    print('---%d---%d' % (i, n))
    if n == 1:
        global i
        i = i + 1
        print('第%d步：将%d号盘子 从%s移动到%s' % (i, n, a, c))
    else:
        move(n-1, a, c, b)#先讲A上n-1个盘子借助C移动到B上面
        global i
        i = i + 1
        print('第%d步：将%d号盘子 从%s移动到%s' % (i, n, a, c))
        move(n-1, b, a, c)#再将B上n-1个盘子借助A移动到C上面

print(move(3, 'A', 'B', 'C'))
        
#高级特性
L = []
n = 1
while n <= 99:
    L.append(n)        
    n = n + 2
print(L)

#切片
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

print(L[0:3])
print(L[-10:])
print(L[:10:2])#前10个数，每两个取一个
print(L[::5])#所有数，每5个取一个
print(L[:])

#迭代
for i, value in enumerate(['A', 'B', 'C'], 2):
    print(i, value)

#列表生成式
print(list(range(1, 11)))
print([x * x for x in range(1, 11)])#[1x1, 2x2, 3x3, ..., 10x10]
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

import os # 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录

s = 'ABCDEF'
print(s[:3])
print(s[::2])

