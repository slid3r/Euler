#!/usr/bin/python2.7

totalLetters = 0

singles = ["zero","one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["0","1","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hundred = "hundred"
hundredAnd = "hundredAnd"
thousand = "thousand"

for x in range(1, 1001):
	thisSum = 0
	checkString = ""
	numString = str(x)
	thisLength = len(numString)
	if thisLength == 1:
		thisSum = len(singles[x])
		checkString = str(x) + " Check String = " + singles[x] + ": " + str(thisSum)
	elif thisLength == 2:
		numOne = int(numString[0])
		numTwo = int(numString[1])
		if numOne == 1:
			thisSum = len(teens[numTwo])
			checkString = str(x) + " Check String = " + teens[numTwo] + ": " + str(thisSum)
		else:
			if numTwo == 0:
				thisSum = (len(tens[numOne]))
				checkString = str(x) + " Check String = " + tens[numOne] + ": " + str(thisSum)
			else:
				thisSum = len(tens[numOne]) + len(singles[numTwo])
				checkString = str(x) + " Check String = " + tens[numOne] + " " + singles[numTwo] + ": " + str(thisSum)
	elif thisLength == 3:
		numOne = int(numString[0])
                numTwo = int(numString[1])
		numThree = int(numString[2])
		if numTwo == 1:
                        thisSum = len(singles[numOne]) + len(hundredAnd) + len(teens[numThree])
                        checkString = str(x) + " Check String = " + singles[numOne] + " " + hundredAnd + " " + teens[numThree] + ": " + str(thisSum)
		elif numThree == 0 and numTwo != 0:
			thisSum = len(singles[numOne]) + len(hundredAnd) + len(tens[numTwo])
			checkString = str(x) + " Check String = " + singles[numOne] + " " + hundredAnd + " " + tens[numTwo] + ": " + str(thisSum)
		elif numTwo == 0 and numThree != 0:
                        thisSum = len(singles[numOne]) + len(hundredAnd) + len(singles[numThree])
                        checkString = str(x) + " Check String = " + singles[numOne] + " " + hundredAnd + " " + singles[numThree] + ": " + str(thisSum)
		elif numTwo == 0 and numThree == 0:
                        thisSum = len(singles[numOne]) + len(hundred)
                        checkString = str(x) + " Check String = " + singles[numOne] + " " + hundred + ": " + str(thisSum)
		else:
			thisSum = len(singles[numOne]) + len(hundredAnd) + len(tens[numTwo]) + len(singles[numThree])
			checkString = str(x) + " Check String = " + singles[numOne] + " " + hundredAnd + " " + tens[numTwo] + " " + singles[numThree] + ": " + str(thisSum)
	elif thisLength == 4:
                numOne = int(numString[0])
		thisSum = len(singles[numOne]) + len(thousand)
		checkString = str(x) + " Check String = " + singles[numOne] + " " + thousand + ": " + str(thisSum)
	thisNewTotal = totalLetters + thisSum
	print(checkString)
	print("New Total = " + str(totalLetters) + "+" + str(thisSum) + " = " + str(thisNewTotal))	
	totalLetters += thisSum
			 
print("Total Letters: " + str(totalLetters))
