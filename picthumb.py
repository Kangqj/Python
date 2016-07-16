#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
im = Image.open('/Users/mac/Python/test.png')
print(im.format, im.size, im.mode)
# width = input('please input thumb width:')
# height = input('please input thumb height:')
im.thumbnail(60, 60)
im.save('thumb.jpg', 'JPEG')