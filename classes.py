# this is the start of the first file. Insert classes here:

import os.path

FAR_file = open('far_files.txt', 'r')
far_files = FAR_file.read()
FAR_file.close()

inventoried_file = open('db_files.txt', 'r')
inventoried_files = inventoried_file.read()
inventoried_file.close()



print(far_files)
print(inventoried_files)
common_entries = set(far_files) & set(inventoried_files)

print(common_entries)