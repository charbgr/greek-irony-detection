import csv

with open('all(epishmeiomena).csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')

	writerUnlabeled = csv.writer(open('test_data.csv', 'w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
	writerLabeled = csv.writer(open('train_data.csv', 'w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')

	writerUnlabeled.writerow(["tweet", "spokenScore","rarityScore","meaningScore","lexicalScore","emoticonScore", "isIronic"])
	writerLabeled.writerow(["tweet", "spokenScore","rarityScore","meaningScore","lexicalScore","emoticonScore", "isIronic"])
	
	#skip header
	next(reader)
	
	for row in reader:
		tweet,spokenScore,rarityScore,meaningScore,lexicalScore,emoticonScore,isIronic = row[0], row[1], row[2], row[3], row[4], row[5], row[6]
		
		if len(isIronic) == 0:
			writerUnlabeled.writerow([tweet, spokenScore,rarityScore,meaningScore,lexicalScore,emoticonScore, "?"])
		else:
			if isIronic == '0':
				isIronic = False
				writerLabeled.writerow([tweet, spokenScore,rarityScore,meaningScore,lexicalScore,emoticonScore,isIronic])
			else:
				isIronic = True
				writerLabeled.writerow([tweet, spokenScore,rarityScore,meaningScore,lexicalScore,emoticonScore,isIronic])

