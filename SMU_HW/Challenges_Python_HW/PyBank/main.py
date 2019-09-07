#currentdir = os.path.realpath(__file__)
#file = currentdir
date = []
money = []
change = []
months = int(0)
total = int(0)
average = int(0)
increase = int(0)
increase_date = str("")
decrease = int(0)
decrease_date = str("")
file = 'C:/Users/sadva/SMU_Coursework/SMU_HW/Challenges_Python_HW/PyBank/budget_data.csv'
import os
import csv
with open (file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        months += 1
        total += int(row[1])
        date.append(row[0])
        money.append(float(row[1]))
        for i in range(1, months):
            change.append(money[i - 1] - money[i])
            if money[i - 1] - money[i] < increase:
                increase = money[i - 1] - money[i]
                increase_date = date[i]
            elif money[i - 1] - money[i] > decrease:
                decrease = money[i - 1] - money[i]
                decrease_date = date[i]
    average = sum(change)/months

print("")
print("Financial Analysis")
print("------------------")
print("Total Months: ", months)
print("Total: $", total)
print("Average Change: $", round(average, 2))
print("Greatest Increase in Profits: ", increase_date, "($", round(increase), ")")
print("Greatest Decrease in Profits: ", decrease_date, "($", round(decrease), ")")