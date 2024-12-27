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


# Function to generate lists for comparison
def getList(data):
    for line in data:
        a = line.strip()
        b = a.split(" ")
        reportList.append(b)
    #print(reportList)
    return reportList

def safeReports(input):
    for line in input:
        print(line)
        if line[1] > line[0]:
            #print("ASC")
            for i in range(len(line)-1):
                ascCount = 0
                i = i+1
                if line[i] > line[i-1]:
                    print(str(line[i]) + " " + str(line[i-1]))
                    limit = int(line[i]) - int(line[i-1])
                    if limit > 3:
                        ascCount = ascCount +1 
                        #print(ascCount)
            if ascCount == 0:
                orderedReports.append(line)
        else:
            #print("DSC")
            for x in range(len(line)-1):
                dscCount = 0
                x = x+1
                if line[x] < line[x-1]:
                    print(str(line[x]) + " " + str(line[x-1]))
                    limit = int(line[x]) - int(line[x-1])
                    if limit > 3:
                        dscCount = dscCount + 1
            if dscCount == 0:
                orderedReports.append(line)
    print(len(orderedReports))
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