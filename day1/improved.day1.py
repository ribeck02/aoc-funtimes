# Advent of Code
#
# Day 1
#
# Author: Richard
#
# Date: 25/12/2024

# Imports
import argparse, os
from argparse import ArgumentParser

# Initialise lists
leftList = []
rightList = []
differenceList = []
similarityList = []

# Function to generate lists for comparison
def getList(data):
	for line in data:
		a = line.strip()
		b = a.split("   ")
		leftList.append(b[0])
		rightList.append(b[1])
	leftList.sort()
	rightList.sort()
	processedList = list(zip(leftList, rightList))
	return processedList

# Function to calculate the difference between list[0] and list[1]
def calculateDifferences(myList):
	for i, value in enumerate(myList):
		if int(value[0]) > int(value[1]):
			temp = int(value[0]) - int(value[1])
		else:
			temp = int(value[1]) - int(value[0])
		differenceList.append(temp)
	return differenceList

# Function to calculate the similarity score
def similarityScore(input):
	column1 = []
	column2 = []
	for line in input:
		column1.append(line[0])
		column2.append(line[1])
	for item in column1:
		if column2.count(item) > 0:
			multiplier = column2.count(item)
			temp = int(item) * int(multiplier)
			similarityList.append(temp)
	return similarityList

# As you can see, this is pretty much identical to your code
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="myFile", help="Open specified file")
args = parser.parse_args()
myFile = args.myFile

# Function calls
sourceData = open(myFile)
processedList = getList(sourceData)
calculateDifferences(processedList)
similarityScore(processedList)
print(sum(differenceList))
print(sum(similarityList))