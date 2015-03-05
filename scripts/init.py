if __name__ == '__main__':

	#nltk
	print 'Initialize nltk'
	import nltk
	nltk.download('omw')
	nltk.download('wordnet')

	#then download ell: http://compling.hss.ntu.edu.sg/omw/

	#Rarity
	print 'Initialize rarity'
	import rarity
	rarity.writeRarities()

	