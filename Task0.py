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

# print the first text and the final call.
first_texts = texts[0]
final_calls = calls[-1]


print("First record of texts, {} texts {} at time {} ".format(
	first_texts[-3],
	first_texts[-2],
	first_texts[-1]
	))
print("Last record of calls, {} calls {} at time {},lasting {} seconds ".format(
	final_calls[-4],
	final_calls[-3],
	final_calls[-2],
	final_calls[-1]
	))