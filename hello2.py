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

#filter()
def is_odd(n):
	return n % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 9 ,10, 15])))
#计算素数的一个方法是埃氏筛法
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)

for n in primes():
	if n < 10:
		print(n)
	else:
		break

#回数是指从左向右读和从右向左读都是一样的数
def is_palindrome(n):
	s = str(n)
	if len(s) == 1:
		return n
	else:
		r = True
		i = 0
		for x in s:
			a = s[i];
			b = s[len(s) - 1 - i]
			i = i + 1
			if a != b:
				r = False
		if r == True:
			return n

output = filter(is_palindrome, range(1, 1000))
print(list(output))

s = 'ABCDEF'
print(s[::-1])

def hunstools(x):
    return str(x) == str(x)[::-1]

outlist = filter(hunstools,range(1,1000))
print(list(outlist))

print(str(12321), str(12321)[::-1])
print(str(12321) == str(12321)[::-1])

#sorted 排序算法
print(sorted([1, 9, 5, 7, -8, 3, 2, 6, ]))
print(sorted([1, 9, 5, 7, -8, 3, 2, 6, ], key = abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0]

L1 = sorted(L, key=by_name)
print(L1)

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score, reverse = True)
print(L2)
