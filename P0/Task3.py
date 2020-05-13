"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

codes=set()
total_calls=0
bang_calls=0
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        call1=call[0].split(")")
        if call1[0][0]=='(':
            if call1[0].split("(")[1] =="080":
                total_calls+=1
                call2=call[1].split(")")
                if call2[0][0]=='(':
                    codes.add(call2[0].split("(")[1])
                    if call2[0].split("(")[1]=="080":
                        bang_calls+=1
                call22=call[1].split(" ")
                if call22[0][0]=='7' or call22[0][0]=='8' or call22[0][0]=='9':
                    codes.add(call22[0][:4])
                if call22[0][:3]=="140":
                    if "140" not in codes:
                        codes.add('140')
                     
                
       
        
    
print("The numbers called by people in Bangalore have codes:")  
for key in sorted(codes):
    print(key)
     

print(str("%.2f" %(bang_calls*100/total_calls))+" percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
