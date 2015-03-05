import re

greek_regx    = re.compile(r'[Α-ώ]+', re.DOTALL)
prosodic_regx = re.compile(r'([Α-ώ])\1{2,}', re.DOTALL)
link_regx     = re.compile(r'http://', re.DOTALL)

lexical_words   = ['σα', 'σαν', 'σάν']
lexical_symbols = ['!', '?', ';']

def giveScore(tweet):

	score = 0
	found_link = True if re.findall(link_regx, tweet) else False
	
	#avoid "... http://""
	if not found_link:
		dots_found = tweet.count('.')
		score += 1 if dots_found >= 2 else 0

	score += sum(1 for symbol in lexical_symbols if tweet.count(symbol) > 1)

	tweet = " ".join(re.findall(greek_regx, tweet)).lower()

	score += sum(1 for token in tweet.split() if token in lexical_words or re.findall(prosodic_regx, token))

	#score += sum(1 for token in tweet.split() if re.findall(prosodic_regx, token))



	return score