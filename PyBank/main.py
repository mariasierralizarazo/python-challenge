import os 
import csv
total_amount = 0
total_months = 0
average = 0
counter = 2
greatest_profits = []
greatest_losses = []

path_file = os.path.join('Resources','budget_data.csv')
#print(f'This is the path file {path_file}')

with open(path_file,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # next skip the row - header
    csv_header = next(csvreader)
    list_file = list(csvreader)
total_months = len(list_file)
average = (float(list_file[total_months-1][1])-float(list_file[0][1]))/(total_months-1)
for item in list_file:
    total_amount= total_amount+ float(item[1])

  
    
    #average = list_file{}


#average = average/total_months

# with open(path_file) as csvfile:
#     file_reader=csv.reader(csvfile,delimiter=',')
#     file_header=next(file_reader)
#     print(f'File header: {file_header}')
#     months_num = len(lis`t(file_reader))
#     for row in file_reader:
#         print(row)
#         print('Aqui')
        #total_amount = total_amount + row[1]
print("\n Financial Analysis")
print("------------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: {total_amount}')
print(f'Average Change: {"%.2f" % average}')
print("------------------------------------------\n")    
