def palin(string):
	if string == "".join(list(reversed(string))):
		return 1;
	return 0;

def symmmetry(string):
	l = len(string);
	if l%2==0:
		m = l//2;
		if string[:m] == string[m:]:
			return 1;
	else:
		m = l//2;
		if string[:m] == string[m+1:]:
			return 1;
	return 0;
	
strs = [];
for i in range(int(input())):
	strs.append(str(input()).lower());
for s in strs:
	pal = palin(s);
	sym = symmmetry(s);
	if pal and sym:
		print("Both property");
	elif pal:
		print("Palindrome");
	elif sym:
		print("Symmetry");
	else:
		print("No property");
