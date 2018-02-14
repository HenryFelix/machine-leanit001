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

"""
creast blank list and add iterable the number into the list.
divide into text and calls separately.
"""

telnumber_text = []
for text in texts:
	if text[0] not in telnumber_text:
		telnumber_text.append(text[0])
	if text[1] not in telnumber_text:
		telnumber_text.append(text[1])

telnumber_call = []
for call in calls:
	if call[0] not in telnumber_call:
		telnumber_call.append(call[0])
	if call[1] not in telnumber_call:
		telnumber_call.append(call[1])

print("there are {} different telephone numbers in the records.".format(len(telnumber_text)+len(telnumber_call)))

"""
TASK 1: 
How many different telephone numbers are there in the records? 
Print a message: 
"There are <count> different telephone numbers in the records."
"""
