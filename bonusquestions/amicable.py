n1 = int(input());
n2 = int(input());
if n1 < 0 or n2 < 0:
	print("Invalid input");
def getdivisors(num):
	divisors = [i for i in range(1,num) if num % i==0];
	return divisors;
if sum(getdivisors(n1)) == n2 and sum(getdivisors(n2)) == n1:
	print("Yes");
else:
	print("No");