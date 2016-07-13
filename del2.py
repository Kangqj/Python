#!/usr/bin/env python
#http://blog.csdn.net/cnmilan/article/details/17968391
import os
import shutil

delList = []
delDir = "/Users/kangqijun/aaa"
delList = os.listdir(delDir)

filePath = os.path.join( delDir, delList[0])
if os.path.isfile:
	os.remove(filePath)
	print filePath + " was removed!"
elif os.path.isdir(filePath):
	shutil.rmtree(filePath, True)
	print "Directory: " + filePath +" was removed!"


# for f in delList:
#     filePath = os.path.join( delDir, f)
#     if os.path.isfile(filePath):
#         os.remove(filePath)
#         print filePath + " was removed!"
#     elif os.path.isdir(filePath):
#     	shutil.rmtree(filePath,True)
#         print "Directory: " + filePath +" was removed!"
