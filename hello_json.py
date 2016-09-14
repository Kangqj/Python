#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#添加可执行权限：chmod a+x hello.py


#序列化－json

#如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
#但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
#JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

import json
import pickle

d = dict(name='bob', age=20, score=88)
print(json.dumps(d))

json_str = '{"age":20, "score":88, "name":bob}'
f = json.loads(json_str)
print(json.load(f))
