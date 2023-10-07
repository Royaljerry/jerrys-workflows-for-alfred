#!/usr/bin/python3

import sys
import os

def swtch (current_level, last_level):
	if current_level == last_level: return "sibling"
	if current_level > last_level: return "child"
	if current_level < last_level: return "parent"

def main():
	# input
	script_folder = os.getcwd()
	project_folder = sys.argv[1]
	data_file = sys.argv[2]
	
	# parse
	data_object = open(data_file)
	data_lines = data_object.readlines()
	data_object.close()
	# print('--> script_folder', script_folder)
	# print('--> project_folder', project_folder)
	# print('--> data_lines', data_lines)

if __name__ == '__main__':
	main()
