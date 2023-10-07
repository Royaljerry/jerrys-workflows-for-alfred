# ##################
# # IMPORT MODULES #
# ##################

import os
import sys
import datetime
import alfred

# #############
# # FUNCTIONS #
# #############

def swtch (cLev, lLev):
	if cLev == lLev: return "sibling"
	if cLev > lLev: return "child"
	if cLev < lLev: return "parent"

# ########
# # MAIN #
# ########

def main():
	# Initialize arguments
	# Get data
	data = alfred.args2()[0]
	# Get working folder
	data_sp = data.split('/')
	wFolder = ('/').join(data_sp[:len(data_sp) - 1])
	wFile =('').join(data_sp[len(data_sp) - 1:])
	# Get folder structure
	data_obj = open(data)
	dataLines = data_obj.readlines()
	data_obj.close()
	# Change to the working folder
	os.chdir(wFolder)
	lLevel = 0
	sFolder = ""
	fError = False
	# Parse lines and create folders
	for s in dataLines:
		# ToDo: make this option selectable by an argument
		cST = s.rstrip("\n")
		# cST = s.rstrip("\n").replace(" ", "_")
		cSTemp = cST.replace("%date%", str(datetime.date.today()))
		cLevel = cSTemp.rfind("\t")+1
		cS = cSTemp.lstrip("\t")
		doLev = swtch(cLevel, lLevel)
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
		print('Alfred has created the folders as defined in "' + str(wFile) + '"')

# #######
# # RUN #
# #######

if __name__ == '__main__':
	main()
