import os
import csv

csvpath = os.path.join(".", "Resources", "election_data.csv")
 
candidates = {}
count = 0
votes = 0
percentage = 0
most_votes = 0
results = ""

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    
    for row in csvreader:
        
        candidate = row[2]
        count = count + 1
        if candidate in candidates.keys():
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
    
    for candidate in candidates:
        votes += candidates[candidate]
    
        percentage = (candidates[candidate])/(count) * (100)
        print(f"{candidate}: {int(percentage)}% {votes}")
        
        if candidates[candidate] > most_votes:
            results = candidate
            most_votes = candidates[candidate]
            
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {count}")
print("----------------------------------------")
print(f"Winner: {results}")
print("----------------------------------------")

with open("result.txt", "w") as text_file:
    print("Election Results", file = text_file)
    print("----------------------------------------", file = text_file)
    print(f"Total Votes: {count}", file = text_file)
    print("----------------------------------------", file = text_file)
    for candidate in candidates:
        print(f"{candidate}: {int(percentage)}% {votes_cast}", file = text_file)
    print("----------------------------------------", file = text_file)
    print(f"Winner: {results}", file = text_file)
    print("----------------------------------------", file = text_file)