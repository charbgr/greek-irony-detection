import re
import csv

spoken_regx = re.compile(r'(\-[Α-ώ\s][^\-]*){2,}|(\*[Α-ώ\s]+\*)', re.DOTALL)


def giveScore(tweet):
	
	result = re.findall(spoken_regx, tweet)
	score = 1 if result else 0
	
	return score

def debugSpoken():
	tweets = {}

	with open('all.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')

		for row in reader:
			tweet = row[1]
			result = re.findall(spoken_regx, tweet)
			spoken_result = 1 if result else 0
			tweets[tweet] = spoken_result
			if spoken_result == 1:
				print(tweet)

	with open('spoken.csv', 'w') as fp:
		writer = csv.writer(fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
		for tweet, spoken in tweets.iteritems():
			writer.writerow([tweet, spoken])

if __name__ == '__main__':
	debugSpoken()