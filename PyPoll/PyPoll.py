import os 
import csv

election_csv = os.path.join("Resources", "election_data.csv")

candidates = []
all_candidates = []
percent_list = []
data = {}
total = 0

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader:
        total += 1
        all_candidates.append(row[2])

        if row[2] in candidates:
            continue
        else:
            candidates.append(row[2])
    total -= 1

for i in range(1, len(candidates)):
    count = 0
    for j in range(len(all_candidates)):
        if candidates[i] == all_candidates[j]:
            count += 1 
    data[candidates[i]] = count
candidates.remove(candidates[0])
print("Election Results") 
print("----------------------\n") 
print("Total votes: %d"%total) 
print("----------------------\n")
for i in candidates:
    percentage = (float(data[i])/float(total)) * 100
    percent_list.append(percentage)
    print("%s: %f(%d)" %(i, round(percentage), data[i]))
print("----------------------\n")
print("Winner:", candidates[percent_list.index(max(percent_list))])
