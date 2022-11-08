# imports
import os
import csv

# absolute file path
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# source data
budget_data = os.path.join(THIS_FOLDER, 'Resources', 'budget_data.csv')
# output file
PyBank_analysis = os.path.join(THIS_FOLDER, 'analysis', 'PyBank_analysis.txt')

# var declarations and initializations
total_months = 0
net_profit = 0
net_profit_change = 0
profit_change = 0
last_profit_change = 0
average_profit_change = 0
last_row_value = 0
greatest_profit_increase_date = "Month-Date"
greatest_profit_increase_amount = 0
greatest_profit_decrease_date = "Month-Date"
greatest_profit_decrease_amount = 0
date = []
profit_loss = []


# safely open file
with open(budget_data) as csvfile:
    
    # perform calculations on CSV
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip header row
    next(csvreader)

    # get value from first row of data
    row1 = next(csvreader)

    last_row_value = int(row1[1])

    # perform calculations
    for row in csvreader:
        
        # get the change in profit from last time
        profit_change = int(row[1]) - last_row_value

        # update the winner of best and worst net profit
        if profit_change > greatest_profit_increase_amount:
            greatest_profit_increase_amount = profit_change
        
        if profit_change < greatest_profit_decrease_amount:
            greatest_profit_decrease_amount = profit_change
        
        # update net profit
        net_profit += int(row[1])

        #update net profit change
        net_profit_change += profit_change
        
        # Add date & population
        date.append(row[0])
        profit_loss.append(profit_change)

        #update last row value and last profit change
        last_row_value = int(row[1])
        last_profit_change = profit_change


total_months = len(date)
average_profit_change = net_profit_change / total_months
greatest_profit_increase_date = date[profit_loss.index(greatest_profit_increase_amount)]
greatest_profit_decrease_date = date[profit_loss.index(greatest_profit_decrease_amount)]

    
# print analysis to terminal
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${net_profit + int(row1[1])}\n")
print(f"Average Change: ${int(average_profit_change)}\n")
print(f"Greatest Increase in Profits: {greatest_profit_increase_date} (${greatest_profit_increase_amount})\n")
print(f"Greatest Decrease in Profits: {greatest_profit_decrease_date} (${greatest_profit_decrease_amount})")

# write analysis to a new file as output
with open(PyBank_analysis,'w',encoding='utf-8') as file_out:
    file_out.write("Financial Analysis\n")
    file_out.write("----------------------------\n")
    file_out.write(f"Total Months: {total_months}\n")
    file_out.write(f"Total: ${net_profit + int(row1[1])}\n")
    file_out.write(f"Average Change: ${int(average_profit_change)}\n")
    file_out.write(f"Greatest Increase in Profits: {greatest_profit_increase_date} (${greatest_profit_increase_amount})\n")
    file_out.write(f"Greatest Decrease in Profits: {greatest_profit_decrease_date} (${greatest_profit_decrease_amount})")
