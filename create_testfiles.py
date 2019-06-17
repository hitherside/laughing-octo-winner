#!/usr/bin/python
# -*- coding: ascii -*-
from typing import TextIO
from os import path



db_file_list = [
	'/mnt/NAS/inv/GOES-16/ABI-L1b-RadF/20190614/OR_ABI-L1b-RadF-M3C02_G16_s20171671145342_e20171671156109_c20171671156144.nc',
	'/mnt/NAS/inv/GOES-16/ABI-L1b-RadF/20190614/OR_ABI-L1b-RadF-M3C02_G16_s20171671145342_e20171671156109_c20171671156144.nc']

db_files: TextIO = open('db_files.txt', 'w')

for entry in db_file_list:
	entry = entry + '\n'
	print(entry)

for entry in db_file_list:
	db_files.write(entry + '\n')
db_files.close()

far_files_list = ['OR_ABI-L1b-RadF-M3C05_G16_s20171671145342_e20171671156109_c20171671156144.nc',
                  'OR_ABI-L1b-RadF-M3C02_G16_s20171671145342_e20171671156109_c20171671156144.nc']

for entry in far_files_list:
	entry = entry + '\n'
	print(entry)

far_files: TextIO = open('far_files.txt', 'w')
for entry in far_files_list:
	far_files.write(entry + '\n')
far_files.close()

db_barefilenames = []

