#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://blog.csdn.net/cnmilan/article/details/17968391
#删除目标路径下的第一个文件(夹)

import os
import shutil

delDir = "/Users/kangqijun/aaa"

def removeFile(path):
	if os.path.isfile(path):
		os.remove(path)
		print("file:" + path + " was removed!")
	elif os.path.isdir(path):
		shutil.rmtree(path, True)
		print("directory: " + path +" was removed!")

delList = []
delList = os.listdir(delDir)

if len(delList) > 0:
	filePath = os.path.join(delDir, delList[0])
	print('name:' + os.path.basename(filePath))
	removeFile(filePath)
else:
	print("nothing to remove!")
