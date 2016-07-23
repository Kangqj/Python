#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#模块－－－－－－－－－－－－－－－－－－－－－－
#添加可执行权限：chmod a+x hello.py

'a test module'

__author__ = 'kqj'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('hello, world')
	elif len(args) == 2:
		print('hello, %s!' % args[1])
	else:
		print('Too many argument!')

if  __name__ == 'main':
	test()

<<<<<<< HEAD
#面向对象
class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))

bart = Student('bart', 59)
lisa = Student('lisa', 87)
bart.print_score()
lisa.print_score()

#类和实例
#访问限制
#继承和多态
class Animal(object):
	"""docstring for Animal"""
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	

=======
#安装第三方模块  pip3 install Pillow
from PIL import Image
im = Image.open('/Users/kangqijun/Python/test.png')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('thumb.JPEG', 'JPEG')
>>>>>>> 8900fe823b380390d24d14dc7dc8c403726d2278

#获取对象信息
import types
def fn():
	pass

print(type(fn)==types.FunctionType)
print(type(123), type('123'), type(None))
print(isinstance('a', str), isinstance(123, int), isinstance(b'a', bytes))
print(isinstance([1, 2, 3], (list, tuple)), isinstance((1, 2, 3), (list, tuple)))

#所有属性和方法
print(dir('ABC'))
print(len('ABC'), 'ABC'.__len__())
print('ABC'.lower())

class MyDog(object):
	def __len__(self):
		return 100
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
	def len(self):
		return 100

obj = MyDog()
print(len(obj))

print('有属性\'x\'吗？', hasattr(obj, 'x'), obj.x)
print('有属性\'y\'吗？', hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print('有属性\'y\'吗？', hasattr(obj, 'y'), getattr(obj, 'y'), obj.y)
print(getattr(obj, 'x', 404))
print(getattr(obj, 'z', 404))
print(hasattr(obj, 'len'))
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))

fn = getattr(obj, 'power')
print(fn)
print(fn())

#实例属性和类属性
class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name
		age=10

s = Student('bob')
print(s.name)

class AAA(object):
	name = 'student'

a = AAA()
print('a.name1', a.name)
print('AAA.name', AAA.name)

a.name = 'teacher'
print('a.name2', a.name)
print('AAA.name', AAA.name)

del a.name
print('a.name3', a.name)
print('AAA.name', AAA.name)
		






