#!/usr/bin/python3

import os
import sys
import fnmatch
import glob
import pathlib

print('#######################')
print('##DIRECTORY SEARCH#####')
print('#######################')


dir = input('Enter exact dir: ')

print('...CHECKING IF FOLDER {} IS VALID..'.format(dir))

if dir in os.listdir():
	print('FOLDER {} IS VALID'.format(dir))
else:
	print('FOLDER {} IS INVALID'.format(dir))


print('#######################')
print('GENERATING .TXT FILE#')
print('#######################')

#print(dir)

x = dir
#print(x)

for dirpath, dirnames, filenames in os.walk(x):
#	print(dirpath)
	if not filenames:
		continue

	pythonic_files = fnmatch.filter(filenames, '*.txt')
	if pythonic_files:
#		print(pythonic_file)
		for file in pythonic_files:
			print('path: {}/ -- file: {}'.format(dirpath, file))




