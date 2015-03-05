import csv
import json
import re
from collections import defaultdict

rarities = {}
greek_regx = re.compile(r'[Α-ώ]+', re.DOTALL)
RARITY_LIMIT = 3
vectors = { 0 : 0, 1 : 10, 2 : 5, 3 : 2}

def giveScore(tweet):
	score = 0
	tweet = " ".join(re.findall(greek_regx, tweet)).lower()


	tokens = tweet.split()
	for token in tokens:
		rarity_vector = int(rarities.get(token, 0))
		score += vectors[rarity_vector]

	if(len(tokens) == 0 ):
		score = 0
	else:
		score = score/len(tokens)
		score = round(score, 2) #2 decimals

	return score

def writeRarities(srcfile='all.csv', dstfile='rarity.csv'):
	frequencies = {}
	with open(srcfile, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')

		for row in reader:
			tweet = " ".join(re.findall(greek_regx, row[1])).lower()
			for token in tweet.split():
				frequencies[token] = frequencies.get(token, 0) + 1
				

	#avoid_tags = ( '@', "http://" )
	

	with open(dstfile, 'w') as fp:
		writer = csv.writer(fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
		for word, counter in frequencies.items():
			#if word.startswith(avoid_tags) is False and counter <= rarity_limit:
			if counter <= RARITY_LIMIT:
				writer.writerow([word.lower(), counter])
	
def readRarities(srcfile='rarity.csv'):
	rarities = {}
	with open(srcfile, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
		for row in reader:
			word, rarity = row[0], row[1]
			rarities[word] = rarity

	return rarities



if __name__ == '__main__':
	writeRarities()
else:
	rarities = readRarities()
	