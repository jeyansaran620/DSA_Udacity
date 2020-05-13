"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
non=set()
numbers=set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for record in texts:
            non.add(record[1])
            non.add(record[0])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for record in calls:
            numbers.add(record[0])
            non.add(record[1])
            
for number in non:
    if number in numbers:
        numbers.remove(number)
print("These numbers could be telemarketers: ")

for number in sorted(numbers):
    print(number)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

