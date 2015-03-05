import re
import nltk
from nltk.corpus import wordnet as wn

greek_regx = re.compile(r'[Α-ώ]+', re.DOTALL)

def giveScore(tweet):
	tweet = " ".join(re.findall(greek_regx, tweet)).lower()

	score = 0
	for token in tweet.split():
		score += len(wn.synsets(token, lang='ell'))

	return score