import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    
    months = 0
    totalprofit = 0
    difference = 0
    avg_change = 0
    loss = 0
    increase = 0
    decrease = 0

    for row in csv_reader:
        months = months + 1
        totalprofit = totalprofit + (line[1])
        
        if months > 1:
                difference = int(line[1]) - loss
       
        avg_change= avg_change + difference
        loss = int(line[1])

        if difference < decrease:
            decrease = difference
            decreasemonth = line[0]
        
        if difference > increase:
            increase = difference
            increasemonth = line[0]

print(months)
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {months}")
print(f"Total: ${totalprofit}")
print("Average Change: $" + str(round(accumulatedchange / (months-1),2)))
print(f"Greatest Increase in Profits: {increasemonth} (${increase})")
print(f"Greatest Decrease in Profits: {decreasemonth} (${decrease})")

with open("textfile.txt", "w") as text_file:
    print("Financial Analysis", file = text_file)
    print("---------------------------------------------------", file = text_file)
    print("Total Months: ", len(months), file = text_file)
    print("Net Total: $", sum(net_profit_loss), file = text_file)
    print("Average Change: $", round(avg_change), file = text_file)  
    print("Greatest Increase: ", greatest_inc_date, "($", greatest_inc,")", file = text_file)
    print("Greatest Decrease: ", greatest_dec_date, "($", greatest_dec,")", file = text_file)

