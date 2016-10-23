s1, s2 = str(input()), str(input());
i = 0;
for j in range(len(s1)):
	if s1[j] == s2[i]:
		i+=1;
	if i == len(s2):
		print("True");
		break;
if i<len(s2):
	print("False");
