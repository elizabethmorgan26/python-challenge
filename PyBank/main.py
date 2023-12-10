import os
import csv

# Define/initialize variables 
months = []
profit_loss_list = []
row_count_months = 0
net_total_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
csv_path = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(csv_path, newline="") as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
             
    # Read through each row of data after the header
    for row in csv_reader:

        # Increment the variable by 1 during each iteration of the loop to count the number of rows
        row_count_months += 1

        # Net total amount of profit/losses over the entire period 
        #Extract the value from the second column (index 1) and convert it to an integer
        #Add the current month's profit loss to a running total of profit/loss and store it in net_total_profit_loss
        current_month_profit_loss = int(row[1])
        net_total_profit_loss += current_month_profit_loss

        if (row_count_months == 1):
            # Create a conditional statement that makes the first month's value equal to the current month's value
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # Calculate change in profit/losses between the current month and the previous month and store it in profit_loss_change
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Add the value of the first column (index 0) to the list months[] to create a list of month names
            months.append(row[0])

            # Store month-to-month profit/loss changes in the list profit_loss_list[]
            profit_loss_list.append(profit_loss_change)

            # Update the variable to hold the most recent month's value for the next loop 
            previous_month_profit_loss = current_month_profit_loss

    #Use the sum function to return the sum of the elements of a list (profit/loss list) and get the total/cumulative profit/loss over the entire period
    total_profit_loss = sum(profit_loss_list)
    
    #Calculate the average profit or loss per month by dividing the total profit or loss by the number of months minus 1 (to exclude the first month) and round to 2 decimal places
    average_profit_loss = round(total_profit_loss/(row_count_months - 1), 2)

    # Calculate and hold the maximum and minimum values in the profit_loss_list to find the greatest increase and decrease in profit/losses over the entire period
    greatest_increase = max(profit_loss_list)
    greatest_decrease = min(profit_loss_list)

    # Find the index (position) of the greatest increase and decrease values in profit/losses over the entire period
    greatest_increase_index = profit_loss_list.index(greatest_increase)
    greatest_decrease_index = profit_loss_list.index(greatest_decrease)

    # Retrieve the corresponding month name from the months list and assign it to the variables best and worst month
    best_month = months[greatest_increase_index]
    worst_month = months[greatest_decrease_index]

#Display the analysis to the terminal
analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {row_count_months}\n\
Total: ${net_total_profit_loss}\n\
Average Change: ${average_profit_loss}\n\
Greatest Increase in Profits: {best_month} (${greatest_increase})\n\
Greatest Decrease in Losses: {worst_month} (${greatest_decrease})\n'

print(analysis)

#Write into a text file named pybank.txt to be stored in the analysis folder 

txt_file_path = os.path.join("analysis", "pybank_financial_analysis.txt")
with open(txt_file_path,"w") as txt_file:
    txt_file.writelines(analysis) 
    txt_file.close() 