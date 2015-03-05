import sys
import os
import csv
import re

regx = re.compile(r'\".*[^\",]\"', re.DOTALL)

def parse(text):
	regx_text = re.findall(regx, text)
	if regx_text:
		text = regx_text[0][1:-1]

	if len(text) is 0:
		text = None

	return text

if os.path.isfile(sys.argv[1]):

	#read file
	reader = None
	data = {}
	counter = 0
	with open(sys.argv[1], 'rU') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True, quotechar='"')

		#parse
		for row in reader:
			date = parse(row[0])
			status = parse(row[1])
			data[status] = date
			print(row)
			counter += 1

		print("Total: ", counter)

	print("After: ", len(data.keys()))

	#write to file
	file_suffix = "(PARSED)"
	path = os.path.abspath(sys.argv[1]).split('.')
	filename = str(path[0] + file_suffix + ".csv")

	with open(filename, "w") as fp:
		writer = csv.writer(fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
		for status, date in data.items():
			writer.writerow([date, status])

else:
	print('select a file')