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

参考#https://github.com/dontlaike/work_uda/blob/a35dc313099e700873ea36d0d9f50654e5dc4f1d/Task4.py

#step1:find no-repeated call when make and receive.
"""
calls_no_repeat_1:make no-repeated outcalling calls
calls_no_repeat_2:received no -repeated calls which has two characteris:
never send texts,receive texts 
"""
calls_no_repeat_1 = []
calls_no_repeat_2 = []

for call in calls:
	if call[0] not in calls_no_repeat_1:
		calls_no_repeat_1.append(call[0])
	if call[1] not in calls_no_repeat_2:
		calls_no_repeat_2.append(call[1])

for text in texts:#add telephone# which send and receive texts
	if text[0] not in calls_no_repeat_2:
		calls_no_repeat_2.append(text[0])
	if text[1] not in calls_no_repeat_2:
		calls_no_repeat_2.append(text[1])

#step2:find the exclused telephone#
telemarketers = list(set(calls_no_repeat_1).difference(set(calls_no_repeat_2)))
telemarketers.sort()

print("These numbers could be telemarketers:")
for i in telemarketers:
	print('\n'+i)


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

