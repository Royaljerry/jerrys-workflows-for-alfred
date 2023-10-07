#!/usr/bin/python3

import sys
import os

def swtch (current_level, last_level):
	if current_level == last_level: return "sibling"
	if current_level > last_level: return "child"
	if current_level < last_level: return "parent"

def main():
	working_folder = os.getcwd()
	data_file = sys.argv[1]
	# print(working_folder)
	# print(data_file)
	data_object = open(data_file)
	data_lines = data_object.readlines()
	data_object.close()
	print(data_lines)


if __name__ == '__main__':
	main()
