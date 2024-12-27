f = open("day1.input", "r")
leftlist = []
rightlist = []
for line in f:
	x = line.split("   ")
	leftlist.append(x[0])
	rightlist.append(x[1])
leftlist.sort()
rightlist.sort()

difference = []
for i, element in enumerate(leftlist):
	if int(element) > int(rightlist[i]):
		temp = int(element) - int(rightlist[i])
	else:
		temp = int(rightlist[i]) - int(element)
	difference.append(temp)
print(sum(difference))
