#regno, name, age, gender, address number, hobby, bloodgroup
# Operation A
file = open("ffcs.csv", "r");
for record in file:
	print(record);
file.close();

#Operation B
file = open("ffcs.csv", "a");
new1 = [str(input()) for i in range(8)];
file.write(','.join(new1));
file.close();

#Operation C
file = open("ffcs.csv", "a+");
new2 = [str(input()) for i in range(8)];
flag = 0;
for record in file:
	if new2[0] in record:
		flag = 1;
		break;
if not flag:
	file.write(",".join(new2));
file.close();

file.write(','.join(new1));
file.close();

#Operation D
malplayers = 0;
file = open("ffcs.csv", "r");
for record in file:
	if "Kerala" in record:
		malplayers+=1;
print(malplayers);

#Operation E
file = open("ffcs.csv", "r");
for record in file:
	if "Tamilnadu" in record and "A+" in record:
		fields = record.split(",");
		print(fields[0], fields[4]);

file.close();