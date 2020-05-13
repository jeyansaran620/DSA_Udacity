"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
numbers=set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for record in texts:
            numbers.add(record[0])
            numbers.add(record[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for record in calls:
            numbers.add(record[0])
            numbers.add(record[1])
            
print("There are "+str(len(numbers))+" different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
