myfile = open ("2600-0.txt")

def duplicate(myfile):
	for words in (myfile):
		word= words.split()
		if word == word:
			print (word,"the word is dupicate")
		else:
			print(word,"the word is not duplicate")
duplicate(myfile)
				
