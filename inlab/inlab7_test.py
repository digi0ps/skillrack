#Inlab 7 ~ digi0ps
# Operation A
def readfile():
	with open("ffcs.csv", "r") as file:
		for record in file:
			print(record,end="");

readfile();

#Operation B
with open("ffcs.csv", "a") as file:
	new1 = [str(input()) for i in range(8)];
	file.write(','.join(new1)+"\n");
readfile();

#Operation C
with open("ffcs.csv", "r+") as file:
	new2 = [str(input()) for i in range(8)];
	flag = 1;
	for record in file:
		if new2[0] == record.split(",")[0]:
			flag = 0;
			break;
	if flag:
		file.write("\n"+",".join(new2));
	readfile();

#Operation D
with open("ffcs.csv", "r") as file:
	malplayers = 0;
	for record in file:
		if "Kerala" in record:
			malplayers+=1;
	print(malplayers);

#Operation E
with open("ffcs.csv", "r") as file:
	for record in file:
		if "Tamilnadu" in record and "A+" in record:
			fields = record.split(",");
			print(fields[1], fields[4]);

#www.github.com/digi0ps