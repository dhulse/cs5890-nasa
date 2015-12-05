#!/usr/bin/python
import pandas as pd
import sys
import re

OBJECT_PAT = re.compile(r'<a.*>(.*)</a>')
CLOSE_APPROACH_DATE_PAT = re.compile(r'(\d+-\w*-\d+)')
TIME_PAT = re.compile(r'\d+-\w*-\d+.*(\d+:\d+)&nbsp;')
LD_PAT = re.compile(r'(.+\.?.+)\/')
AU_PAT = re.compile(r'\/(.+\.?.+)')

def preprocess_df(file_path):
	df = pd.read_csv(file_path, delimiter='|')
	df['time'] = df['close-approach-date']
	df['nominal-LD-distance'] = df['ca-distance-nominal']
	df['nominal-AU-distance'] = df['ca-distance-nominal']
	del df['ca-distance-nominal']
	df['minimum-LD-distance'] = df['ca-distance-minimum']
	df['minimum-AU-distance'] = df['ca-distance-minimum']
	del df['ca-distance-minimum']
	print 'Preprocessing object column'
	df = preprocess_object(df)
	print 'Preprocessing close-approach column'
	df = preprocess_close_approach_date(df)
	print 'Preprocessing time column'
	df = preprocess_time(df)
	print 'Preprocessing distance columns'
	df = preprocess_ld_distance(df)
	df = preprocess_au_distance(df)
	return df

def preprocess_object(df):
	df['object'] = df['object'].apply(transform_object)
	return df

def preprocess_close_approach_date(df):
	df['close-approach-date'] = df['close-approach-date'].apply(transform_close_approach_date)
	return df

def transform_object(obj):
	match = re.search(OBJECT_PAT, obj)
	obj = match.group(1)
	obj = re.sub('&nbsp;', ' ', obj)
	return obj

def preprocess_time(df):
	df['time'] = df['time'].apply(transform_time)
	return df

def preprocess_ld_distance(df):
	df['nominal-LD-distance'] = df['nominal-LD-distance'].apply(transform_ld_distance)
	df['minimum-LD-distance'] = df['minimum-LD-distance'].apply(transform_ld_distance)
	return df

def preprocess_au_distance(df):
	df['nominal-AU-distance'] = df['nominal-AU-distance'].apply(transform_au_distance)
	df['minimum-AU-distance'] = df['minimum-AU-distance'].apply(transform_au_distance)
	return df

def transform_close_approach_date(date):
	return re.search(CLOSE_APPROACH_DATE_PAT, date).group(1)

def transform_time(time):
	return re.search(TIME_PAT, time).group(1)

def transform_ld_distance(distance):
	return re.search(LD_PAT, distance).group(1)

def transform_au_distance(distance):
	return re.search(AU_PAT, distance).group(1)

def main(file_input, file_output):
	df = preprocess_df(file_input)
	df.to_csv(file_output)

# argv = [program, input, output]
if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])