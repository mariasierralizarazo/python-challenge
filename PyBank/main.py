import os 
import csv
total_amount = 0
total_months = 0
profit_diff = 0
losses_diff = 0

path_file = os.path.join('Resources','budget_data.csv')

with open(path_file,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # next skip the row - header
    csv_header = next(csvreader)
    list_file = list(csvreader)
total_months = len(list_file)
average = (float(list_file[total_months-1][1])-float(list_file[0][1]))/(total_months-1)
for i in range(total_months-1):
    total_amount= total_amount+ float(list_file[i][1])
    if (i==0):
        profit_diff = float(list_file[i+1][1])-float(list_file[i][1])
        greatest_profits = list_file[i+1][0]
    elif ((float(list_file[i+1][1])-float(list_file[i][1]))> profit_diff):
        profit_diff = float(list_file[i+1][1])-float(list_file[i][1])
        greatest_profits = list_file[i+1][0]

    if (i==0):
        losses_diff = float(list_file[i+1][1])-float(list_file[i][1])
        greatest_losses = list_file[i+1][0]
    elif((float(list_file[i+1][1])-float(list_file[i][1]))< losses_diff):
        losses_diff = float(list_file[i+1][1])-float(list_file[i][1])
        greatest_losses = list_file[i+1][0]

  
print("\n Financial Analysis")
print("------------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: {total_amount}')
print(f'Average Change: {"%.2f" % average}')
print(f'Greatest Increase in Profits: {greatest_profits} ($ {profit_diff})')
print(f'Greatest Decrease in Profits: {greatest_losses} ($ {losses_diff})')
print("------------------------------------------\n")    
