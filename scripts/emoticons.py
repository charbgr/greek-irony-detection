import re
import csv

emoticon_regex = re.compile(r'((?::|;|=)(?:-|\')?(?:\(|D|P|Ρ|\)))', re.DOTALL)

def giveScore(tweet):
	if(re.findall(emoticon_regex, tweet)):
		#print(re.findall(emoticon_regex, tweet))
		return 1

	return 0

def fixEmoticons():
	with open('all(epishmeiomena).csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
		writer = csv.writer(open('all(epishmeiomena)(fix).csv', 'w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
		writer.writerow(["tweet", "spokenScore","rarityScore","meaningScore","lexicalScore","emoticonScore", "isIronic"])
		next(reader)

		for row in reader:
			tweet,spokenScore,rarityScore,meaningScore,lexicalScore,emoticonScore,isIronic = row[0], row[1], row[2], row[3], row[4], row[5], row[6]
			emoticonScore = giveScore(tweet)
			if(emoticonScore==1):
				print("allakse to tweet : ",tweet)
			writer.writerow([tweet,spokenScore,rarityScore,meaningScore,lexicalScore,emoticonScore,isIronic])



if __name__ == '__main__':
	fixEmoticons()
