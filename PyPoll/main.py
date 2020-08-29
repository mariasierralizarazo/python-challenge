# Dependencies
import os 
import csv
results = []
exist = False
counter = 0
# File path identification
path_file = os.path.join('Resources','election_data.csv')
# File opening
with open(path_file,newline='') as csvfile:
    # Reader declaration
    csvreader = csv.reader(csvfile, delimiter=',')
    # next skip the row - header
    csv_header = next(csvreader)
    # List cretion with file's information
    list_file = list(csvreader)
total_votes = len(list_file)
for item in list_file:
    exist = False
    for i in range(len(results)):
        if item[2] == results[i][0]:
            results[i][1] = results[i][1] + 1
            exist = True
            break

    if exist == False:
       results.append([item[2],1])

# Terminal printing
print("\nElection Results")
print("------------------------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------------------------")
for item in results:
    percentage = (item[1]*100)/total_votes
    print(f'{item[0]}: {"%.3f" % percentage}% ({item[1]})')
    counter = counter+1
    if counter==1:
        winner = item[0]
        win_percentage = percentage
    elif percentage > win_percentage:
        winner = item[0]
        win_percentage = percentage
print("------------------------------------------") 
print(f'Winner: {winner}')   
print("------------------------------------------") 