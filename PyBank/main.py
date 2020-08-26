import os 
import csv
path_file = os.path.join('Resources','budget_data.csv')
#print(f'This is the path file {path_file}')
with open(path_file, newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    file_header=next(reader)
    #print(f'File header: {file_header}')
