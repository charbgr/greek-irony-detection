import csv

import rarity
import spoken
import meanings
import lexical
import emoticons

import os
import sys

if __name__ == '__main__':

	filename = sys.argv[1]
	basename = os.path.basename(filename).split('.')[0]

	with open(sys.argv[1], 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
		writer = csv.writer(open(basename+"(epishmeiomeno).csv", 'w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')

		writer.writerow(['tweet', 'spoken', 'rarity', 'meanings', 'lexical', 'emoticons', 'isIronic'])
		counter = 0
		for row in reader:
			date, tweet = row[0], row[1]

			spokenScore = spoken.giveScore(tweet)
			rarityScore = rarity.giveScore(tweet)
			meaningScore = meanings.giveScore(tweet)
			lexicalScore = lexical.giveScore(tweet)
			emoticonScore = emoticons.giveScore(tweet)
			isIronic = ""
			
			writer.writerow([tweet, spokenScore, rarityScore, meaningScore, lexicalScore, emoticonScore, isIronic])

			#if counter >= 5:
			#	break
			counter += 1
