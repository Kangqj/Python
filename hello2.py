#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#添加可执行权限：chmod a+x hello.py


# map/reduce
# map: map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
	return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print (list(r))
print (list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#reduce reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce
def add(x, y):
	return x + y

print(reduce(add, [1, 3, 5, 7 ,9]))

def fn(x, y):
	return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))

def char2num(s):
	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

print(reduce(fn, map(char2num, '13579')))

def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
	return reduce(fn, map(char2num, s))

print(str2int('12345'))

# def strtoint():
# 	return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# print(strtoint('123456'))

def normalize(name):
	i = 0
	s = ''
	for x in name:
		#方法1
		# name = name.title()
		# return name
		#方法2
		if i == 0:
			x = x.upper()
		else:
			x = x.lower()
		s = s + x
		i = i + 1
	return s

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(ls):
	def fax(a, b):
		return a * b
	return(reduce(fax, ls))

print('3*5*7*9=', prod([3, 5, 7, 9]))

def char2num(s):
		return {'.':0.1, '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
a = map(char2num, '123.456')
print(list(a))

def str2float(s):
	if s.find('.') == -1:
		return reduce(lambda x, y: x*10 + y, map(int, s))
	else:
		a, b = s.split('.')#将s根据.来分隔成两个list
		b = '0' + b
		print(a,'\n',b)
		print(b[::-1])#将list中的元素反转
		return reduce(lambda x, y: x*10 + y, map(int, a)) + reduce(lambda x, y: x*0.1 + y, map(int, b[::-1]))
	
print(str2float('123.456'))

def test(s):
	t = reduce(lambda x, y: x *10 + y, map(int, s))
	l = 10**len(s)# ** 表示乘方, 即就是10的4次方
	print(t,l)
	print(t/l)

test('1234')

