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
	# print('--> script_folder', script_folder)
	# print('--> project_folder', project_folder)
	# print('--> data_lines', data_lines)
	os.chdir(project_folder)

	lLevel = 0
	sFolder = ""
	fError = False
	# Parse lines and create folders
	for s in data_lines:
		# ToDo: make this option selectable by an argument
		cST = s.rstrip("\n")
		# cST = s.rstrip("\n").replace(" ", "_")
		cSTemp = cST.replace("%date%", str(datetime.date.today()))
		cLevel = cSTemp.rfind("\t")+1
		cS = cSTemp.lstrip("\t")
		doLev = get_level(cLevel, lLevel)
		if doLev == "child":
			os.chdir(sFolder)
		if doLev == "parent":
			pDif = lLevel - cLevel
			for i in range(pDif):
				os.chdir("..")
		try:
			os.mkdir(cS)
		except Exception:
			error = True
		lLevel = cLevel
		sFolder = cS
	# print('Creating folders OK')
	if fError == True:
		print('Creating folders failed. :(')
	if fError == False:
		print('Alfred has created the folders as defined in "' + str(project_folder) + '"')


if __name__ == '__main__':
	main()
