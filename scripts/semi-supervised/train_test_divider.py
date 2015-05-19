import csv
import sys
from os import listdir
from os.path import isfile, join, abspath


party_filespath = None
parties_files = None

party_filespath = sys.argv[1] if sys.argv[1:] else "../../dataset/Parties Before the Elections/"
parties_files = [ abspath(party_filespath + f) for f in listdir(party_filespath) if isfile(join(party_filespath,f)) and f.endswith(('(PARSED).csv')) ]

labeled_data_path = abspath("labeled_data.csv")

for party in parties_files:
	tweets = {}

	with open(party, 'r') as party_csvfile:
		p_reader = csv.reader(party_csvfile, delimiter=',', skipinitialspace=True, quotechar='"')
		for row in p_reader:
			date, tweet = row[0:]
			tweets[tweet] = None #ignore value

	with open(labeled_data_path, 'r') as labeled_csvfile:
		l_reader = csv.reader(labeled_csvfile, delimiter=',', quotechar='\'', lineterminator='\n')

		output_writer = csv.writer(open('train_data_without__'+ party.split('/')[-1], 'w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
		output_writer.writerow(["tweet", "spokenScore","rarityScore","meaningScore","lexicalScore","emoticonScore", "isIronic"])

		for row in l_reader:
			
			try:
				tweet, spokenScore, rarityScore, meaningScore, lexicalScore, emoticonScore, isIronic = row[0:]
			except Exception as e:
				correct_idx = len(row) - 7
				tweet = ''.join(row[:correct_idx+1])
				spokenScore, rarityScore, meaningScore, lexicalScore, emoticonScore, isIronic = row[correct_idx+1:]

			if tweet not in tweets.keys():
				output_writer.writerow([tweet, spokenScore,rarityScore,meaningScore,lexicalScore,emoticonScore,isIronic])
