#!/usr/bin/python2.7

monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
monthDaysLeap = [31,29,31,30,31,30,31,31,30,31,30,31]
monthNames = ["January","February","March","April","May","June","July","August","September","October","November","December"]
weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
myNumofDays = sum(monthDays)
myStartDay = 2
arrayToUse = []
firstSunday = 0

for i in range(1, 101):
	myMonthNameIndex = 0
	myYearNumber = 1900 + i
	if myYearNumber % 4 == 0:
		arrayToUse = monthDaysLeap
	else:
		arrayToUse = monthDays
	for x in arrayToUse:
		for y in range(1, (x+1)):
			if myStartDay == 7:
				myStartDay = 0
			if y == 1 and myStartDay == 6:
				print("Adding a Sunday to current count: " + str(firstSunday))
				firstSunday += 1
			print(str(myYearNumber) + ": " + monthNames[myMonthNameIndex] + " " + str(y) + " " + weekDays[myStartDay] + " " + str(myStartDay))
			myStartDay += 1
		myMonthNameIndex += 1	

print("Final Sunday Count: " + str(firstSunday))
