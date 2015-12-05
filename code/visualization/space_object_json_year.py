#!/usr/bin/python
import sys
import pandas as pd
from datetime import datetime as dt

def get_datetime(date_str):
	return dt.strptime(date_str, '%Y-%b-%d')

def in_year_range(date_str, min, max):
	print date_str
	year = get_year(date_str)
	if year >= min and year <= max:
		return True
	else:
		return False

def main(input_file_path, output_file_path, min_year, max_year):
	df = pd.read_csv(input_file_path)
	df['datetime'] = df['close-approach-date'].apply(get_datetime)
	min_year = dt(min_year, 1, 1)
	max_year = dt(max_year, 12, 31)
	df = df[df['datetime'] >= min_year]
	df = df[df['datetime'] <= max_year]
	del df['close-approach-date']

	with open(output_file_path, 'w') as outfile:
		print 'Reading distances...'
		lst_content = ''
		outfile.write('{\n')
		outfile.write('\t"distance": [')
		for distance in df['nominal-AU-distance']:
			lst_content +=  str(distance) + ','
		lst_content = lst_content.strip(',')
		outfile.write(lst_content)
		outfile.write('],\n')

		print 'Reading names...'
		lst_content = ''
		outfile.write('\t"name": [')
		for name in df['object']:
			lst_content += '"%s",' % name
		lst_content = lst_content.strip(',')
		outfile.write(lst_content)
		outfile.write('],\n')

		print 'Reading dates...'
		lst_content = ''
		outfile.write('\t"date": [')
		for date in df['datetime']:
			theta = date.timetuple().tm_yday * 360 / 365
			lst_content += str(theta) + ','
		lst_content = lst_content.strip(',')
		outfile.write(lst_content)
		outfile.write(']\n')
		outfile.write('}')

# input_file_path output_file_path, min_year, max_year
if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))