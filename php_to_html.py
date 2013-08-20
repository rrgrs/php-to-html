#!/usr/bin/env python

import os
import subprocess
import sys

from optparse import OptionParser

usage = 'usage: %prog src-dir dest-dir'
parser = OptionParser(usage=usage)


args = parser.parse_args()[1]

source = args[0]
destination = args[1]

if not os.path.isdir(source):
	raise Exception('make sure source is a dir')

if os.path.isfile(destination):
	raise Exception('destination file already exists')

if not os.path.isdir(destination):
	os.makedirs(destination)

if destination[-1] != '/':
	destination += '/'

ignored_files = (
	'.svn',
	'.git',
	'.DS_Store',
)

def is_ignored(file_path):
	for ignored_file in ignored_files:
		if file_path[:len(ignored_file)] == ignored_file:
			return True
	return False

for dir_info in os.walk(source):
	path = dir_info[0]
	if is_ignored(path):
		continue
	if path[-1] != '/':
		path += '/'
	destination_path = destination + path.replace(source, '')
	files = dir_info[2]
	for file_full in files:
		if is_ignored(file_full):
			continue
		file_name, file_extension = os.path.splitext(file_full)
		if file_extension == '.php':
			file_contents = subprocess.Popen(['php', path + file_full], stdout=subprocess.PIPE).communicate()[0].replace('.php', '.html')
			file_full = file_name + '.html'
		else:
			file_handle = open(path + file_full, 'r')
			file_contents = file_handle.read()
			file_handle.close()
		if not os.path.isdir(destination_path):
			os.makedirs(destination_path)
		destination_file_handle = open(destination_path + file_full, 'w+')
		destination_file_handle.write(file_contents)
		destination_file_handle.close()
