# Set Imports so Python can read CSV
import os
import csv

# Set values to start at zero and make values variables for python to use math
time = []
profit_changes = []
time_minus_one_profit = 0
time_zero_profit = 0
profit_change = 0
total_time = 0
total_profit = 0

# Creates the path that python can follow from PyBank to the Resources file to use information contained in the Budget CSV
budgetcsv = os.path.join("Resources", "Budget.csv")

# Opens CSV
with open(budgetcsv, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    # Set the parameters to read the header then the is.
    csv_header = next(csvfile)
    for i in reader:

        #Totals the profits over the entire Time Horizon
        total_time += 1
        time_zero_profit = int(i[1])
        total_profit += time_zero_profit

        if (total_time == 1):
            time_minus_one_profit = time_zero_profit
            continue

        else:

            #Calulates Profit Change and resets value for the next calculation.
            profit_change = time_zero_profit - time_minus_one_profit
            time.append(i[0])
            profit_changes.append(profit_change)
            #Resets the value of the previous time horizon point to the next to continue the calculations.
            time_minus_one_profit = time_zero_profit

    #sum and average of the changes in "Profit/Losses" over the entire period
    total_change = sum(profit_changes)
    average_change = round(total_change/(total_time - 1), 2)

    #Finds greates increase and loss
    greatest_increase = max(profit_changes)
    greatest_loss = min(profit_changes)

    #Finds high and low month in the entire Time Horizon
    highest_month_index = profit_changes.index(greatest_increase)
    lowest_month_index = profit_changes.index(greatest_loss)

    #Determine high and low months
    high_month = time[highest_month_index]
    low_month = time[lowest_month_index]

#Prints "Financial Analysis" and a spacer
print("Financial Analysis")
print("----------------------------")

#Prints Totals for Time and Profit
print(f"Total time:  {total_time}")
print(f"Total:  ${total_profit}")

#Prints Changes(Average as well as Greatest Increase and Decrease)
print(f"Average Change:  ${average_change}")
print(f"Greatest Increase in Profits:  {high_month} (${greatest_increase})")
print(f"Greatest Decrease in Losses:  {low_month} (${greatest_loss})")


#Prints/Exports the data to a new file
with open("SummaryData.txt", "w") as text_file:

    print("Financial Analysis",  file=text_file)
    print("----------------------------",  file=text_file)

    print(f"Total time:  {total_time}",  file=text_file)
    print(f"Total:  ${total_profit}",  file=text_file)

    print(f"Average Change:  ${average_change}",  file=text_file)
    print(f"Greatest Increase in Profits:  {high_month} (${greatest_increase})", file=text_file)
    print(f"Greatest Decrease in Losses:  {low_month} (${greatest_loss})", file=text_file)