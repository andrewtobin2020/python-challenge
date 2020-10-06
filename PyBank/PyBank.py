import os
import csv
import numpy

bank_csv = os.path.join("Resources", "budgetdataHW03.csv") 

# Initialize variable
monthCount = 0
totalAmount = 0
prValue = 0
diff = 0
diffMax = 0
diffMin = 0

with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    first_row = next(csvreader)
    monthCount += 1
    totalAmount += int(first_row[1])
    prev_net = int(first_row[1])

    print('Financial Analysis' + '\n')
    print("-----------------------" + '\n')
   
    for i in csvreader:
        month = i[0]
        amount = i[1]
        intamount = int(amount)
        #diff = intamount - prValue

        if diffMax < diff:
            diffMax = diff
            diffMaxDate = month
        
        if diffMin > diff:
            diffMin = diff
            diffMinDate = month
        prValue = intamount

        monthCount = monthCount + 1
        totalAmount += int(amount)
        averageDiff = sum(diff)/len(diff)

print("Total Months: "+ str(monthCount))
print("Total: $ " + str(totalAmount))
print("Average Change: $ " + str(averageDiff))
print("Greatest increase in profits: " + str(diffMaxDate) + ": $" + str(diffMax))
print("Greatest Decrease in profits: " + str(diffMinDate) + ": $" + str(diffMin))