import os
import csv
import statistics

bank_csv = os.path.join("Resources", "budgetdataHW03.csv") 

# Initialize variable
monthCount = 0
totalAmount = 0
prValue = 0
diff = 0
diffMax = 0
diffMin = 0

with open(bank_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    print(f'Financial Analysis' + '\n')
    print(f"-----------------------" + '\n')

    for i in csvreader:
        month = i[0]
        amount = i[1]
        intamount = int(amount)
        diff = intamount - prValue

        if diffMax < diff:
            diffMax = diff
            diffMaxDate = month
        
        if diffMin > diff:
            diffMin = diff
            diffMinDate = month
        prValue = intamount

        monthCount = monthCount + 1
        totalAmount += int(amount)
        averageDiff = statistics.mean(diff)

print(f'Total Months: {monthCount}')
print(f"Total: $ {totalAmount}")
print(f"Average Change: $ + {averageDiff}")
print(f"Greatest increase in profits: {diffMaxDate} : ($ {diffMax})")
print(f"Greatest Decrease in profits: {diffMinDate} : ($ {diffMin})")