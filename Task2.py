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

#step1:create a function which build a dictionary includes phone and call duration.
call_time = {}
max_duration = 0

def check_call_time(phone,call_duration):
	"""
	iterable the phone and call duration from dictionary.
	"""

	if phone in call_time:
		call_time[phone] += int(call_duration)
	else:
		call_time[phone] = int(call_duration)

#step2:use above function and iterable the original calls list.
for call in calls:
	check_call_time(call[0],call[3])
	check_call_time(call[1],call[3])

#step3:output the result as max phone# and max time duration.递归自身
for phone in call_time:
	if call_time[phone] > max_duration:
		max_duration = call_time[phone]
		max_call = phone

print("{} spent the longest time,{} seconds,on the phone during September 2016.".format(max_call,max_duration))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message: 
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.". 

HINT: Build a dictionary with telephone numbers as keys, and their
total time spent on the phone as the values. You might find it useful
to write a function that takes a key and a value and modifies a 
dictionary. If the key is already in the dictionary, add the value to
the key's existing value. If the key does not already appear in the
dictionary, add it and set its value to be the given value.
"""



