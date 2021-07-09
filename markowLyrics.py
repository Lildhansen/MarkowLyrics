import string, random

#the strings are not allowed to end in a newline - this should be fixed - see findPossibleStartingLetters(text):
pangram = "The quick brown fox jumps over the lazy dog"
lyrics = """'Cause I'm as free as a bird now
And this bird you cannot change
Oh, oh, oh, oh
And the bird you cannot change
And this bird, you cannot change"""

shakespeare = """When forty winters shall beseige thy brow,
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
And see thy blood warm when thou feel'st it cold."""

HP = """Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly
normal, thank you very much. They were the last people you’d expect to be involved in anything
strange or mysterious, because they just didn’t hold with such nonsense.
 Mr. Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy
man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin
and blonde and had nearly twice the usual amount of neck, which came in very useful as she
spent so much of her time craning over garden fences, spying on the neighbors. The Dursleys
had a small son called Dudley and in their opinion there was no finer boy anywhere.
 The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was
that somebody would discover it. They didn’t think they could bear it if anyone found out about
the Potters. Mrs. Potter was Mrs. Dursley’s sister, but they hadn’t met for several years; in fact,
Mrs. Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing
husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the
neighbors would say if the Potters arrived in the street. The Dursleys knew that the Potters had a
small son, too, but they had never even seen him. This boy was another good reason for keeping
the Potters away; they didn’t want Dudley mixing with a child like that.
 When Mr. and Mrs. Dursley woke up on the dull, gray Tuesday our story starts, there was
nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be
happening all over the country. Mr. Dursley hummed as he picked out his most boring tie for
work, and Mrs. Dursley gossiped away happily as she wrestled a screaming Dudley into his high
chair.
 None of them noticed a large, tawny owl flutter past the window.
 At half past eight, Mr. Dursley picked up his briefcase, pecked Mrs. Dursley on the cheek, and
tried to kiss Dudley good-bye but missed, because Dudley was now having a tantrum and
throwing his cereal at the walls. """


#prøv at indsætte en ordbog måske. så burde den give en masse rigtige ord


availableChars = string.ascii_lowercase + ",. \n':!-;’"


def findProbabilityMatrix(text):
	text = text.lower()
	foundLetters = ""
	emptyOccurrenceDict = createEmptyDictOfOccurrences()
	occurrenceDict = findOccurrenceDict(emptyOccurrenceDict,text)
	probDict = findProbabilityDict(occurrenceDict)	
	y = []
	probMatrixInProgress = list(probDict.values())
	probMatrix = []
	for theDics in probMatrixInProgress:
		column = []
		for v in theDics.values():
			column.append(v)
		probMatrix.append(column)
	return probMatrix

def createEmptyDictOfOccurrences():
	return {letter:{key:0 for key in availableChars} for letter in availableChars}

def findOccurrenceDict(emptyOccurrenceDict,text):
	for index,letter in enumerate(text):
		#print(letter) - if letter wasnt found
		if index != len(text)-1:
			emptyOccurrenceDict[letter][availableChars[availableChars.index(text[index+1])]] +=1
	return emptyOccurrenceDict #which is not empty anymore

def findProbabilityDict(occurrenceDict):
	for letter,precedingLetters in occurrenceDict.items():
		totalOccurrencesForLetter = 0
		for precedingLetter,occurrences in precedingLetters.items():
			totalOccurrencesForLetter += occurrences
		for precedingLetter,occurrences in precedingLetters.items():
			if totalOccurrencesForLetter == 0:
				break
			occurrenceDict[letter][precedingLetter] /= totalOccurrencesForLetter
	return occurrenceDict #which is now probDict


def findPossibleStartingLetters(text):
	listOfLines = text.split("\n")
	return [letter[0] for letter in listOfLines]

def findIntialStateVector(text):
	listOfLines = findPossibleStartingLetters(text)
	occurrenceStateVector = findOccurrenceStateVector(listOfLines)
	occurrenceSum = sum(occurrenceStateVector)
	intialStateVector = [value/occurrenceSum for value in occurrenceStateVector]
	return intialStateVector


def findOccurrenceStateVector(listOfLines):
	occurrenceStateVector = []
	listOfLinesLower = turnAllElementsInListIntoLowerCase(listOfLines)
	for char in availableChars:
		counter = 0
		while char in listOfLinesLower:
			counter += 1
			listOfLinesLower.remove(char)
		occurrenceStateVector.append(counter)
	return occurrenceStateVector

def turnAllElementsInListIntoLowerCase(inputList):
	return [char.lower() for char in inputList]

testMatrix = [[1,2,10],[3,4,20],[5,6,30]] #læses som:
"""
 1  3  5
 2  4  6
10 20 30
"""

def calculateSquareMatrixToThePowerOf(matrix,t): #cheat solution - use numpy's https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_power.html
	oldMatrix = matrix.copy()
	while t > 1:
		matrix = squareMatrixMultiplication(matrix,oldMatrix)
		t -= 1
	return matrix
	
def squareMatrixMultiplication(matrix1,matrix2):
	size = len(matrix1)
	newMatrix = []
	for column in matrix2:
		i = 0
		newMatrixColumn = []
		while i < size: #måske len(newMatrixColumn) i stedet for "i". tror det er det samme
			newMatrixValue = 0
			for j,value in enumerate(column):
				newMatrixValue += value*matrix1[j][i]
			newMatrixColumn.append(newMatrixValue)
			i+=1
		newMatrix.append(newMatrixColumn)
	return newMatrix


testMatrix = [[1,2],[3,4],[5,6]]
testVector = [10,20]

def squareMatrixVectorMultiplication(matrix,vector):
	size = len(matrix)
	if size != len(vector): #if dimensions dont match
		return
	newMatrix = []
	i = 0
	while i < size:
		j = 0
		newMatrixValue = 0
		while j < size:
			newMatrixValue += matrix[j][i]*vector[j]
			j += 1
		newMatrix.append(newMatrixValue)
		i += 1
	return newMatrix

def isSquareMatrix(matrix):
	return len(matrix[0]) == len(matrix)

def calcProbabilityVector(intialStateVector,probabilityMatrix,t):
	if not isSquareMatrix(probabilityMatrix):
		return
	matrixToThePowerOf = calculateSquareMatrixToThePowerOf(probabilityMatrix,t)
	return squareMatrixVectorMultiplication(matrixToThePowerOf,intialStateVector)



def createNewText(chars,text):
	initState = findIntialStateVector(text)
	probMatrix = findProbabilityMatrix(text)
	finalText = "".join(random.choices(availableChars,weights=initState))
	i = 1
	while i < chars:
		probVector = calcProbabilityVector(initState,probMatrix,i)
		finalText += "".join(random.choices(availableChars,weights=probVector))
		i+=1
	return finalText



simple = "Peter Hansen"
#hvordan kan "Peter Hansen" give "pensr". der er jo kun et s og her er det 100% chance for at det næste bogstav er e


print(createNewText(5,simple))
#der er en fejl et eller andet sted fordi den gør noget der er 0% chance for.
#et problem er også at vi kun kigger på "order" 1, altså vi ser kun på et bogstav og hvad der følger det.
	#vi burde tage højere order, så hvis der fx står "ther", er der stor sandsynlighed for den næste er "e"
		#ved order 1, kigger vi kun på hvad der kommer efter r


#todo:
"""

calc probMatrix
do markow stuff
	check notes

webscraper to get lyrics from bands - takes random song from top 10/20/50/100


"""