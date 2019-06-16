# this is the start of the first file. Insert classes here:

import os.path

FAR_file = open('FAR_filenames.txt', 'r')
far_files = FAR_file.readlines()
FAR_file.close()

inventoried_file = open('inventoried_filenames.txt', 'r')
inventoried_files = inventoried_file.readlines()
inventoried_file.close()

sample_file = open('sample_files.txt', 'r')
sample_files = sample_file.readlines()
sample_file.close()

print(far_files)
print(inventoried_files)
print(sample_files)

print(far_files)