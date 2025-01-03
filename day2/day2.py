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
safeReports = []
badReports = []
fixedReports = []
unfixedReports = []
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

def reportChecker(input):
    global safeReports
    global badReports
    global notOrdered
    for line in input:
        if int(line[1]) > int(line[0]): # logic for assumed ascending
            notOrdered = 0 # counter
            badGap = 0 # counter
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
            if int(badGap) == 0 and int(notOrdered) == 0: # if counters == 0 it's a safe report
                safeReports.append(line)
            else:
                badReports.append(line) # add to unsafe report list
        else: # logic for assumed descending
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
                safeReports.append(line)
            else:
                badReports.append(line)
    print(len(safeReports))
    print(len(badReports))
    reportFixer(badReports)
    return safeReports

def reportFixer(input):
    global badReports
    global fixedReports
    global unfixedReports
    for line in input:
        if int(line[1]) > int(line[0]): # logic for assumed ascending
            notOrdered = 0 # counter
            badGap = 0 # counter
            for i in range(len(line)-1):
                i = i+1
                if int(line[i]) > int(line[i-1]):
                    limit = int(line[i]) - int(line[i-1])
                    if int(limit) > 3 or int(limit) < 1:
                        badGap = badGap + 1
                else:
                    notOrdered = notOrdered + 1
            if (int(badGap) == 1 and int(notOrdered) == 0) or (int(badGap) == 0 and int(notOrdered) == 1):
                fixedReports.append(line)
            else:
                unfixedReports.append(line) # add to unsafe report list
        else: # logic for assumed descending
            notOrdered = 0
            badGap = 0
            for x in range(len(line)-1):
                x = x+1
                if int(line[x]) < int(line[x-1]):
                    limit = int(line[x-1]) - int(line[x])
                    if int(limit) > 3 or int(limit) < 1:
                        badGap = badGap + 1
                else:
                    notOrdered = notOrdered + 1
            if (int(badGap) == 1 and int(notOrdered) == 0) or (int(badGap) == 0 and int(notOrdered) == 1):
                fixedReports.append(line)
            else:
                unfixedReports.append(line)
    print(len(fixedReports))
    print(len(unfixedReports))
    for i in fixedReports:
       print(i)
    # for i in orderedReports:
    #     print(i)
    return fixedReports

# ArgParse
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="myFile", help="Open specified file")
args = parser.parse_args()
myFile = args.myFile

# Function calls
sourceData = open(myFile)
getList(sourceData)
#print(reportList)
reportChecker(reportList)
#print(len(orderedReports))
