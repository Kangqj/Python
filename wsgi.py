#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#模块－－－－－－－－－－－－－－－－－－－－－－
#添加可执行权限：chmod a+x hello.py

# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'<h1>Hello, web!</h1>']

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
    
# 	f = open('/Users/kangqijun/Python/hello.html', 'r')
#     body = f.read()
#     f.close()
#     return [body.encode('utf-8')]
    