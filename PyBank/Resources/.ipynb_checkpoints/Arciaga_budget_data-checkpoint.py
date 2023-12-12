# Import modules os and csv

import os
import csv

# Set the path for PyBank Budget Data csv

PyBankcsv = os.path.join("..", "Resources", "budget_data.csv")
                         
# Create variables
                    
count = 0
total_profit = 0
total_change_profits = 0                         
initial_profit = 0 
previous_profit = 0

# Create increase & decrease variables
greatest_increase = ["", float ("-inf")]
greatest_decrease = ["", float ("inf")]
            
# Create a list to store changes in profit for each month

profit_changes = []

# with open(PyBankcsv, encoding='utf-8') as csvfile:
with open(PyBankcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next (csvreader)
    
    # Calculate total number of months included in the dataset 
    for row in csvreader:
        count = count + 1
        
        # Calculate the net total amount of "Profit/Losses" over the entire period
        current_profit = int (row [1]) 
        total_profit = total_profit + current_profit
        
        # Calculate the changes in "Profit/Losses" over the entire period 
        if count > 1: 
            change = current_profit - previous_profit
            
            # Append the change to the list
            profit_changes.append(change)
            
            # Calculate the greatest increase in profits (date and amount) over the entire period 
            if change > greatest_increase [1]:
                greatest_increase [1] = change
                greatest_increase [0] = row [0]
        
            # Calculate the greatest decrease in profits (date and amount) over the entire period  
            if change < greatest_decrease [1]:
                greatest_decrease [1] = change
                greatest_decrease [0] = row [0]
        
        # Update previous profit for next iteration 
        previous_profit = current_profit

# Calculate the total changes in profit
total_change_profits = sum(profit_changes)

# Then calculate the average of those changes 
average_change = total_change_profits / len(profit_changes)
        
#Print the results      
text_output = "Financial Analysis\n" 
text_output += "----------------------------\n"
text_output += f"Total Months: {count}\n"
text_output += f"Total: ${total_profit}\n"
text_output += f"Average Change: ${average_change: .2f}\n"
text_output += f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
text_output += f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"

print (text_output) 

with open("PyBank Analysis.txt","w") as outputFile: 
    outputFile.write (text_output) 
    