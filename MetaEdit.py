#! /usr/local/bin/python3.6
import os
import csv
from glob import glob 


currentdir = os.getcwd()
curdir = currentdir + '/CSVinput'

hi2 = ''
wrote = False 
if not os.path.exists('CSVupdates'):
	os.mkdir('CSVupdates')
os.chdir(curdir) 
for eachfile in glob('*.csv'):
	if eachfile != 'testchange.csv':
		each_list = eachfile.split('.csv')
		metafile = open(eachfile,'r')
		newfilename = each_list[0] + '_upd.csv'
		
		os.chdir('../CSVupdates')
		newmeta = open(newfilename,'w')
		os.chdir(curdir)
		for line in metafile:
			changecsv = open('testchange.csv','r')
			reader = csv.reader(changecsv, delimiter=",")
			for key in reader:
				wrote = False
				hi2 = key[0]
				if hi2 in line:
					newline = (key[0] + ',' + '"' + key[1] + '"') 
					newmeta.write(str(newline) + '\n')
					wrote = True
					break

			if wrote == False:
				newmeta.write(line)
			changecsv.close()
		
		metafile.close()
		newmeta.close()
	




