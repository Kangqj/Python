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

#安装第三方模块
from PIL import Image
im = Image.open('/Users/mac/Python/test.JPEG')
print(im.format, im.size, im.module)
im.thumbnail((200, 100))
im.save('thumb.JPEG', 'JPEG')

