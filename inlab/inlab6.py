#Inlab 6 ~ digi0ps
n = int(input());
alist = [];
for i in range(n):
	name = str(input());
	author = str(input());
	date = str(input());
	accnum = int(input());
	aval = str(input());
	alist.append(accnum);
target = int(input());

def binarySearch():
	miny = 0;
	maxy = len(alist)-1;
	while maxy >= miny:
		mid = int((miny + maxy)/2);
		if alist[mid] == target:
			return 1;
		elif alist[mid] < target:
			miny = mid + 1;
		else:
			maxy = mid - 1;
	return 0;

if binarySearch() == 1:
	print("Found");
else:
	print("Not found");