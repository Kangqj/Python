#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#添加可执行权限：chmod a+x hello.py

#模块－－－－－－－－－－－－－－－－－－－－－－

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