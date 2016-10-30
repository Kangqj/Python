#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#添加可执行权限：chmod a+x hello.py

import os
from urllib.request import urlopen
import urllib

response = urlopen("http://www.baidu.com")

sp = os.path.join(os.getcwd(), 'response.txt')

f = open(sp, 'w')

f.write(str(response.read()))
f.close()

values = {"username":"xxx", "password":"xxx"}
data = urllib.parse.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
response = urlopen(url)
print(response.read())