# Right now do 1970-2050
# degrees = (YEAR - 1970) * 360 / 80
import sys
import pandas as pd

YEAR = 0

def get_year(date_str):
	fields = date_str.split('-')
	return int(fields[YEAR])

def in_year_range(date_str, min, max):
	print date_str
	year = get_year(date_str)
	if year >= min and year <= max:
		return True
	else:
		return False

def main(file_path, min_year, max_year):
	df = pd.read_csv(file_path)
	df['year'] = df['close-approach-date'].apply(get_year)
	del df['close-approach-date']
	df = df[df['year'] >= min_year]
	df = df[df['year'] <= max_year]

	with open('space-objects.json', 'w') as outfile:
		print 'Reading distances...'
		outfile.write('{\n')
		outfile.write('\t"distance": [')
		for distance in df['nominal-AU-distance']:
			outfile.write(str(distance) + ',')
		outfile.write('\n\t],\n')

		print 'Reading dates...'
		outfile.write('\t"date": [')
		for year in df['year']:
			theta = (year - min_year) * 360 / 80
			outfile.write(str(theta) + ',')
		outfile.write('\n\t]\n')
		outfile.write('}')

if __name__ == '__main__':
	main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))