"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
numbers={}

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for record in calls:
        if numbers.get(record[0])==None:
            numbers[record[0]]=int(record[3])
        else:
            numbers[record[0]]+=int(record[3])
            
        if numbers.get(record[1])==None:
            numbers[record[1]]=int(record[3])
        else:
            numbers[record[1]]+=int(record[3])

    high=0
    number=''
    for key in numbers:
        if numbers[key]>high:
            high=numbers[key]
            number=key
print(str(number) +" spent the longest time, "+str(high) +" seconds, on the phone during September 2016.")      
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

