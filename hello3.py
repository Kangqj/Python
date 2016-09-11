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


#安装第三方模块  pip3 install Pillow
# from PIL import Image
# im = Image.open('/Users/kangqijun/Python/test.png')
# print(im.format, im.size, im.mode)
# im.thumbnail((200, 100))
# im.save('thumb.JPEG', 'JPEG')

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
<<<<<<< HEAD

#面向对象编程, 使用__slots__
class Student(object):
	pass

s = Student()
s.name = 'michael'
print(s.name)

def set_age(self, age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

def set_score(self, score):
	self.score = score

#面向对象高级编程
#试用__slots__
class Student(object):
	__slots__=('name', 'age',)
s = Student()
s.name = 'aaa'
s.age = 23

class GraduateStudnet(object):
	pass
g = GraduateStudnet()
g.score = 999

#试用@property
class Student(object):
	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an interger!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100')
		self._score = value
	@property
	def birth(self):
		return self._birth
	
	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
		return 2015 - self._birth


s = Student();
s.score = 60


class Screen(object):

	@property
	def width(self):
		return self._width
	@width.setter
	def width(self, value):
		self._width = value;

	@property
	def height(self):
		return self._height
	@height.setter
	def height(self, value):
		self._height = value;

	@property
	def resolution(self):
		return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)

#多重继承

