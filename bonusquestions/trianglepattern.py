from math import factorial
inp = []; #Input List
n = int(input());
#Getting Input
for i in range(n):
		col = [int(input()) for j in range(i+1)]
		inp.append(col);

p = factorial(n); #Possibilities 
out = [0 for i in range(p)];

for ele in inp:
	l = len(ele);
	parts = p//l;
	ele.sort();
	for i in range(l):
		s = parts * i;
		e = parts * (i+1);
		for j in range(s,e):
			out[j]+=ele[i];
print(max(out));