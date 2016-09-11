#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#模块－－－－－－－－－－－－－－－－－－－－－－
#添加可执行权限：chmod a+x hello.py

#序列化
import pickle
import os
d = dict(name = 'Bob', gae = 20, score = 88)
pickle.dumps(d)

print('写入文件->' + os.path.join(os.path.abspath('.'), 'test1.txt'))
#序列化->将数据写入文件
path = os.path.join(os.path.abspath('.'), 'test1.txt')
f = open(path, 'wb')
pickle.dump(d, f)
f.close()

#反序列化->读出数据
f = open(path, 'rb')
d = pickle.load(f)
f.close()
print('读出的数据->', d)

#JSON
import json
