#!/usr/bin/python3

import sys
import os
import datetime

def get_level (current_level, last_level):
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
	os.chdir(project_folder)

	last_level = 0
	working_folder = ""
	script_error = False
	
	for line in data_lines:
		# ToDo: make this option selectable by an argument (What is this?)
		current_line = line.rstrip("\n")
		current_line_temp = current_line.replace("%date%", str(datetime.date.today()))
		current_level = current_line_temp.rfind("\t")+1
		current_line_temp_stripped = current_line_temp.lstrip("\t")
		do_level = get_level(current_level, last_level)
		if do_level == "child":
			os.chdir(working_folder)
		if do_level == "parent":
			folder_difference = last_level - current_level
			for i in range(folder_difference):
				os.chdir("..")
		try:
			os.mkdir(current_line_temp_stripped)
		except Exception:
			error = True
		last_level = current_level
		working_folder = current_line_temp_stripped
	
	if script_error == True:
		print('Creating folders failed. :(')
	if script_error == False:
		print('Alfred has created the folders as defined in "' + str(project_folder) + '"')

if __name__ == '__main__':
	main()
