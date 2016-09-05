#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#模块－－－－－－－－－－－－－－－－－－－－－－
#添加可执行权限：chmod a+x hello.py


#IO编程

#读取文本文件，且是utf-8编码格式的文本文件
try:
	f = open('/Users/kangqijun/Python/test1.txt', 'r')
	print('---\n' + f.read())
finally:
	if f:
		f.close()

with open('/Users/kangqijun/Python/test1.txt', 'r') as f:
	print('---\n' + f.read())

f = open('/Users/kangqijun/Python/test1.txt', 'r')
for line in f.readlines():
	print('---\n' + line.strip())# 把末尾的'\n'删掉
f.close()

f = open('/Users/kangqijun/Python/test1.txt', 'r')
# print('1---\n' + f.readline(8))
print('2---\n' + f.read(6))

f = open('/Users/kangqijun/Python/test1.txt', 'r', encoding='utf-8', errors='ignore')
print(f.read())

f = open('/Users/kangqijun/Python/test1.txt', 'r', encoding='gbk', errors='ignore')
print(f.read())

#读取二进制文件：图片，视频，等,使用‘rb’
# f = open('/Users/kangqijun/Python/test.png', 'rb')
# print(f.read())# 十六进制表示的字节

#写文件

with open('/Users/kangqijun/Python/test1.txt', 'w') as f:
	f.write('hello, world')

with open('/Users/kangqijun/Python/test1.txt', 'r') as f:
	print(f.read())



