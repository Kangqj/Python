#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('git status')
s1 = input('do you want to commit (y/n)?:')
if len(s1) == 1 & s1.isalpha():
	if s1 == 'y':
		print('git add .')
		msg = input('please input commit message:')
		print('git commit -m \"%s\"' % msg)
		s2 = input('do you want to push this commit (y/n)?:')
		if len(s2) == 1 & s2.isalpha():
			if s2 == 'y':
				print('git push')
else:
	print('Invalid input !');
	

