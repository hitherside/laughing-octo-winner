# this is the start of the first file. Insert classes here:

from os import path

far_files = []
FAR_file = open('far_files.txt', 'r')
for line in FAR_file:
    far_files.append(line.rstrip())
FAR_file.close()

inventoried_files = []
inventoried_file = open('db_files.txt', 'r')
for line in inventoried_file:
    inventoried_files.append(line.rstrip())
inventoried_file.close()

print('far_files')
for entry in far_files:
    print(path.basename(entry))

print('inventoried_files')
for entry in inventoried_files:
    print(path.basename(entry))



