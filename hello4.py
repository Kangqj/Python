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

#StringIO和BytesIO 在内存中读写str
from io import StringIO
f = StringIO()
f.write('hello world')
print('output:' + f.getvalue())

f = StringIO('hello!\nhi\ngoodbye')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

#操作文件和目录
import os
import os.path

print('->' + os.name)#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.uname())

#环境变量
# print(os.environ)#所有环境变量
print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))

#查看当前目录的绝对路径
print('->' + os.path.abspath('.'))
#合成路径
print('->' + os.path.join('/Users/kangqijun', 'testdir'))
# os.mkdir('/Users/kangqijun/testdir')
# os.rmdir('/Users/kangqijun/testdir')

#拆分路径
print(os.path.split('/Users/kangqijun/testdir'))
print(os.path.splitext('/Users/kangqijun/testdir'))#可以得到文件的扩展名

# os.rename('/Users/kangqijun/testdir/test.m', 'test1.m')

#获取当前路径
print('->' + os.getcwd())

#改变当前路径
os.chdir(r'/Users/kangqijun/testdir')
print('->' + os.getcwd())

#判断当前路径是否存在
print(os.path.exists('/Users/kangqijun/testdir'))
print(os.path.isdir('/Users/kangqijun/testdir'))
print(os.path.isfile('/Users/kangqijun/testdir'))

if os.path.exists('/Users/kangqijun/testdir1') == False:
	os.mkdir('/Users/kangqijun/testdir1')
	print('mk dir success !')










