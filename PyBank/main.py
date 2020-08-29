# Dependencies
import os 
import csv
# Variables to save the information
total_amount = 0
total_months = 0
profit_diff = 0
losses_diff = 0
# File path identification
path_file = os.path.join('Resources','budget_data.csv')
# File opening
with open(path_file,newline='') as csvfile:
    # Reader declaration
    csvreader = csv.reader(csvfile, delimiter=',')
    # next skip the row - header
    csv_header = next(csvreader)
    # List cretion with file's information
    list_file = list(csvreader)
# The number of months will be equal to the list's length
total_months = len(list_file)
# The average change will be equal to (last_month_amount - First_month_amount)/(last_month_number - first_month_number)
average = (float(list_file[total_months-1][1])-float(list_file[0][1]))/(total_months-1)
# Loop for getting the sum of the total amount, and the greatest values (decreases and increases)
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

# Terminal printing
print("\nFinancial Analysis")
print("------------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${"%.2f" % average}')
print(f'Greatest Increase in Profits: {greatest_profits} ($ {profit_diff})')
print(f'Greatest Decrease in Profits: {greatest_losses} ($ {losses_diff})')
print("------------------------------------------\n")    
#.txt File expotation
L = "Financial Analysis\n"+"------------------------------------------\n"+'Total Months: '+ str(total_months)+ '\n'
L = L + 'Total: $'+ str(total_amount)+'\n'+ 'Average Change: $' + str("%.2f" % average) + '\n'
L = L + 'Greatest Increase in Profits: '+ str(greatest_profits)+ '($'+ str(profit_diff)+')\n'
L = L + 'Greatest Decrease in Profits: '+ str(greatest_losses)+ '($'+ str(losses_diff)+')\n'
L = L + "------------------------------------------"
# Export the results to text file
txt_file_path = os.path.join('Resources','Output_file.txt')
with open(txt_file_path, "w") as txt_file:
    txt_file.write(L)