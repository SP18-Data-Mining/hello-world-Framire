import csv 
import sys
tracker = 0
listOfLines = []
currentDistance = sys.maxint
currentLabel = '0'
testTracker = 0
with open("FruitData.csv", "rb") as file:
	input = csv.reader(file, delimiter = ",")
	for l, line in enumerate(input):
		if tracker > 0: 
			if tracker % 5 != 0:
				listOfLines.append(line)
		if tracker >0:
			if tracker % 5 == 0:
				t = line
				for r in listOfLines:		
					thisDistance = ((float(r[3]) - float(line[3]))**2) - ((float(r[4]) - float(line[4]))**2)
					if(thisDistance < currentDistance):
						t = r
						currentDistance = thisDistance
						cuurentLabel = r[0]
				print("Closest Thing to your line")
				print t
				print("Line " + str(tracker) + " has the following label: " + t[0])
				print (line)
				print("New Test:\n")
				testTracker = testTracker + 1
				currentDistance = sys.maxint 
		tracker = tracker + 1