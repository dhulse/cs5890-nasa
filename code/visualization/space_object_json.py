#!/usr/bin/python
import space_object_json_year as so
import sys

def main(input_file_path):
	for i in xrange(1970, 2202):
		print 'Reading Year: ' + str(i)
		so.main(input_file_path, 'space_object_files/' + str(i) + '.json', i, i)

# file_input_path
if __name__ == '__main__':
	main(sys.argv[1])