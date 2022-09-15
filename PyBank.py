import csv
import math as m
import pandas as pd

# Open the CSV
with open('budget_data.csv') as csv_file:
    header = next(csv_file)
    csv_reader = csv.reader(csv_file, delimiter=',')
    date_count = 0
    total = 0
    profit = 0

    for row in csv_reader:
        # calculate how many months are in the data set
        date_count += 1
        # calculate the total amount of profit/losses over the entire period
        total= int(row[1])
    # calculate the average of the changes in profit/losses over the entire period
    

print(f"Total Months: {date_count}")
print(f"Total: $ {total}")
# print(f"Average Change: $ {average}")
# print(f"Greatest Increase in Profits: {greatest_increase}")
# print(f"Greatest Decrease in Profits: {greatest_decrease}")
# print(Greatest_Increase)

csv_file.close()