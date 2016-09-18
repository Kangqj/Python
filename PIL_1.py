#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#添加可执行权限：chmod a+x hello.py

from PIL import Image, ImageFilter
im = Image.open("test.png")
im2 = im.filter(ImageFilter.BLUR)#模糊滤镜
im2.save('filter.jpg', 'jpeg')
im2.show()
