# Advent of Code
#
# Day 1
#
# Author: Richard
#
# Date: 26/12/2024

# Imports
import argparse, os
from argparse import ArgumentParser

# Initialise lists
reportList = []
orderedReports = []
notOrdered = 0


# Function to generate lists for comparison
def getList(data):
    global reportList
    for line in data:
        a = line.strip()
        b = a.split(" ")
        reportList.append(b)
    #print(reportList)
    return reportList

def safeReports(input):
    global orderedReports
    global notOrdered
    for line in input:
        if int(line[1]) > int(line[0]):
            notOrdered = 0
            badGap = 0
            for i in range(len(line)-1):
                i = i+1
                if int(line[i]) > int(line[i-1]):
                    limit = int(line[i]) - int(line[i-1])
                    if int(limit) > 3 or int(limit) < 1:
                        badGap = badGap + 1
                        break
                else:
                    notOrdered = notOrdered + 1
                    break
            if int(badGap) == 0 and int(notOrdered) == 0:
                orderedReports.append(line)
        else:
            notOrdered = 0
            badGap = 0
            for x in range(len(line)-1):
                x = x+1
                if int(line[x]) < int(line[x-1]):
                    limit = int(line[x-1]) - int(line[x])
                    if int(limit) > 3 or int(limit) < 1:
                        badGap = badGap + 1
                        break
                else:
                    notOrdered = notOrdered + 1
                    break
            if int(badGap) == 0 and int(notOrdered) == 0:
                orderedReports.append(line)
    print(len(orderedReports))
    # for i in orderedReports:
    #     print(i)
    return orderedReports

# ArgParse
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="myFile", help="Open specified file")
args = parser.parse_args()
myFile = args.myFile

# Function calls
sourceData = open(myFile)
getList(sourceData)
#print(reportList)
safeReports(reportList)
#print(len(orderedReports))
