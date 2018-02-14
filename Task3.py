"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#part1

#step1:create a list called from Bangalore.
from_Bangalore = []
for i in range(len(calls)):
	if calls[i][0].startswith("(080)"):
		from_Bangalore.append(calls[i][1])

#参考https://github.com/dontlaike/work_uda/blob/a35dc313099e700873ea36d0d9f50654e5dc4f1d/Task3.py
#step2:choose the phone# which has three characteries.
final_Bangalore= []
for phone in from_Bangalore:
	"""fixed telephone
	"""
	if phone[1] =='0' and phone.find('(') and phone.find(')'):
		call_f =phone[0:phone.find(')')]
		if call_f not in final_Bangalore:
			final_Bangalore.append(call_f)
	"""mobile telephone
	"""
	if phone[0] =='7' or phone[0] =='8' or phone[0]=='9':
		call_m =phone[0:4]
		if call_m not in final_Bangalore:
			final_Bangalore.append(call_m)

#step3:delete the duplicated and sort.
final_Bangalore = sorted(list(set(final_Bangalore)))

#step4:output the results
print("The numbers called by people in Bangalore have codes:")
for i in final_Bangalore:
	    print(i)

#part2
#input the percentage for 080.
eight_Bangalore =[]
for phone in from_Bangalore:
	if phone[0:3].startswith("(080)"):
		eight_Bangalore.append("(080)")

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(len(eight_Bangalore)/len(final_Bangalore)))

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
