import string

pangram = "The quick brown fox jumps over the lazy dog"
lyrics = """'Cause I'm as free as a bird now
And this bird you cannot change
Oh, oh, oh, oh
And the bird you cannot change
And this bird, you cannot change"""

shakespeare = """
When forty winters shall beseige thy brow,
And dig deep trenches in thy beauty's field,
Thy youth's proud livery, so gazed on now,
Will be a tatter'd weed, of small worth held:
Then being ask'd where all thy beauty lies,
Where all the treasure of thy lusty days,
To say, within thine own deep-sunken eyes,
Were an all-eating shame and thriftless praise.
How much more praise deserved thy beauty's use,
If thou couldst answer 'This fair child of mine
Shall sum my count and make my old excuse,'
Proving his beauty by succession thine!
This were to be new made when thou art old,
And see thy blood warm when thou feel'st it cold.
"""


availableChars = string.ascii_lowercase + ",. \n':!-"


def findProbabilityMatrix(text):
	text = text.lower()
	foundLetters = ""
	emptyOccurenceDict = createEmptyDictOfOccurences()
	occurenceDict = findOccurenceDict(emptyOccurenceDict,text)
	probDict = findProbabilityDict(occurenceDict)	
	y = []
	probMatrixInProgress = list(probDict.values())
	probMatrix = []
	for theDics in probMatrixInProgress:
		column = []
		for v in theDics.values():
			column.append(v)
		probMatrix.append(column)
	print(probMatrix)

def createEmptyDictOfOccurences():
	return {letter:{key:0 for key in availableChars} for letter in availableChars}

def findOccurenceDict(emptyOccurenceDict,text):
	for index,letter in enumerate(text):
		if index != len(text)-1:
			emptyOccurenceDict[letter][availableChars[availableChars.index(text[index+1])]] +=1
	return emptyOccurenceDict #which is not empty anymore

def findProbabilityDict(occurenceDict):
	for letter,precedingLetters in occurenceDict.items():
		totalOccurencesForLetter = 0
		for precedingLetter,occurences in precedingLetters.items():
			totalOccurencesForLetter += occurences
		for precedingLetter,occurences in precedingLetters.items():
			if totalOccurencesForLetter == 0:
				break
			occurenceDict[letter][precedingLetter] /= totalOccurencesForLetter
	return occurenceDict #which is now probDict


def findPossibleStartingLetters(text):
	listOfLines = text.split("\n")
	return [letter[0] for letter in listOfLines]
	

	

findProbabilityMatrix(shakespeare)


#todo:
"""
lav intial vektor baseret på findPossibleStartingLetters

calc probMatrix
do markow stuff
	check notes

webscraper to get lyrics from bands - takes random song from top 10/20/50/100


"""