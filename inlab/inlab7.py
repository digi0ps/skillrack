def readfile():
	with open("ffcs.csv", "r") as file:
		for record in file:
			print(record,end="");
readfile();
def opB():
	with open("ffcs.csv", "a") as file:
		new1 = [str(input()) for i in range(8)];
		file.write(','.join(new1)+"\n");
	readfile();
def opC():
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
def opD():
	with open("ffcs.csv", "r") as file:
		malplayers = 0;
		for record in file:
			if "Kerala" in record:
				malplayers+=1;
		print(malplayers);
def opE():
	with open("ffcs.csv", "r") as file:
		for record in file:
			if "Tamilnadu" in record and "A+" in record:
				fields = record.split(",");
				print(fields[1], fields[4]);
opB(); opC(); opD(); opE();
#www.github.com/digi0ps
