# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources','election_data.csv')

# Method 1: Plain Reading of CSV files
with open(csvpath, 'r') as election_data:
    csvreader = csv.reader(election_data, delimiter=',')
    csv_header = next(csvreader)

    
    candidates = dict()

#  #  1. Total Number of Votes Cast   #   
    voter_data = []    
    for row in csvreader:
        voter_data.append(row)
        if row[2] in candidates.keys():
            candidates[row[2]]+=1
        else:
            candidates[row[2]]=1
    length = len(voter_data)
    print(f"Election Results")
    print(f"===============")
    print(f"Total Votes: {length}")
    print(f"===============")

    winner = ["",0]

    for key,value in candidates.items():
        if value >winner[1]:
            winner=[key,value]
        print(f'{key}: {round(value/length*100,2)}% ({value})')
    print(f"===============")
    print(f"Winner:  {winner[0]}")
    
    

# export file
output_path = os.path.join('analysis', 'output.txt')

with open(output_path, 'w', newline="") as txtfile:
        # txtfile.write('========================\n') 
        txtfile.write('========================\n')
        txtfile.write(f"Election Results\n")
        txtfile.write('========================\n')
        txtfile.write(f"Total Votes: {length}\n")
        txtfile.write('========================\n')
        for key,value in candidates.items():
            txtfile.write(f'{key}: {round(value/length*100,2)}% ({value})\n')
        txtfile.write('========================\n')
        txtfile.write('========================\n')
        txtfile.close()
   
