# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources','budget_data.csv')

# Method 1: Plain Reading of CSV files
with open(csvpath, 'r') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')
    csv_header = next(csvreader)
   # print(f"CSV Header: {csv_header}")

 #  1. Total Number of Months included in the dataset   
    bank_data = []    
    for row in csvreader:
        bank_data.append(row)
  #  print(bank_data[0])
    Length = len(bank_data)
    print(f"Financial Analysis")
    print(f"-------------------")
    print(f"Total Months: {Length}")

    # 2. Net total amount of Profit/Losses over the entire period
    Sum_amounts = 0
    for row in bank_data:
        Sum_amounts = Sum_amounts + int(row[1])
    print(f"Total : ${Sum_amounts}")

    #  3. Average of the changes in Profit/Losses over the entire period
    change_list = []
    change_sum  = 0
    for i in range(Length-1):
        now_row = bank_data[i]
        next_row = bank_data[i+1]
        change = int(next_row[1]) - int(now_row[1]) 
        change_list.append(change)
        change_sum = change_sum + change
    Length_change_list = len(change_list)
    avg_change = change_sum/Length_change_list
    print(f"Average Change : ${avg_change:.2f}")

        
    #  4.  Greatest increase in profit - dates and amount
    #  5.  Greatest decrease in losses - date and 
    max_profit = 0
    min_profit = 0
    for i in range(Length_change_list):
        current_data = bank_data[i+1]
        current_date = current_data[0]
        profit_loss = change_list[i]
        if profit_loss > max_profit:
            max_profit = profit_loss
            max_date = current_date
        if profit_loss < min_profit:
            min_profit = profit_loss
            min_date = current_date
    print(f"Greatest Increase in Profits: {max_date} ${max_profit}")
    print(f"Greatest Decrease in Profits: {min_date} ${min_profit}")

    output_path = os.path.join('analysis', 'output.txt')
    with open(output_path, 'w', newline="") as txtfile:
        txtfile.write(f"Financial Analysis\n")
        txtfile.write(f"-------------------\n")
        txtfile.write(f"Total Months:  {Length}\n")
        txtfile.write(f"Total: ${Sum_amounts}\n")
        txtfile.write(f"Average Change: ${avg_change:.2f}\n")
        txtfile.write(f"Greatest Increase in Profits: ${max_profit}\n")
        txtfile.write(f"Greatest Decrease in Profits: ${min_profit}\n")
        #txtfile.write(f"Total Month:  {Length}\n")
        #txtfile.write(f"Total Month:  {Length}\n")






   
