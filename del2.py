#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://blog.csdn.net/cnmilan/article/details/17968391
#删除目标路径下的某一文件(夹)

import os
import shutil

delDir = "/Users/kangqijun/aaa"

def removeFile(path):
	if os.path.isfile(path):
		os.remove(path)
		print("delete file:" + path + " was removed!")
	elif os.path.isdir(path):
		shutil.rmtree(path, True)
		print("delete directory: " + path +" was removed!")

def filterDir():
	delList = []
	delList = os.listdir(delDir)
	if len(delList) > 0:
		for name in delList:
			if '2016' in name:
				removeFile(os.path.join(delDir, name))
				break
	else:
		print("nothing to remove!")

# if len(delList) > 0:
# 	print(delList)
# 	filePath = os.path.join(delDir, delList[0])
# 	removeFile(filePath)
# else:
# 	print("less than 20!")
