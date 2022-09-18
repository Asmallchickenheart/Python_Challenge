import csv
import math as m
import pandas as pd

# Open the CSV
with open('/Users/siyuanliang/PycharmProjects/pythonProject/BootCamp_python/budget_data.csv') as csv_file:
    header = next(csv_file)
    csv_reader = csv.reader(csv_file, delimiter=',')
    date_count = 0
    total = 0
    previous_profit = 0
    difference = {}

    for row in csv_reader:
        # calculate how many months are in the data set
        date = row[0]
        date_count += 1
        # calculate the total amount of profit/losses over the entire period
        profit = int(row[1])
        total += profit

        # calculate the average of the changes in profit/losses over the entire period
        change = profit - previous_profit
        difference[date] = change
        previous_profit = profit

    difference.pop(next(iter(difference)))
    average_change = sum(difference.values()) / len(difference)

    # get the max and min change and date
    Greatest_increase = max(difference, key=difference.get)

    Greatest_decrease = min(difference, key=difference.get)

print(f"Total Months: {date_count}")
print(f"Total: $ {total}")
print(f"Average Change: $ {round(average_change, 2)}")
print(f"Greatest Increase in Profits: {Greatest_increase} (${difference[Greatest_increase]})")
print(f"Greatest Decrease in Profits: {Greatest_decrease} (${difference[Greatest_decrease]})")
# print(Greatest_Increase)

csv_file.close()