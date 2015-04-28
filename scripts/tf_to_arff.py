import re

regx = re.compile('[A-z]+')

tf = open('tf.txt', 'r')
writer = open('adadada.txt', 'w')
with open('test_data.arff', 'r') as f:
	for line in f.readlines():
		#print(line)
		val = tf.readline()
		val = regx.match(val).group(0)
		#print(val)
		writer.write(str(line).replace(',?', ","+val))
		

tf.close()