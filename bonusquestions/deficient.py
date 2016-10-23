n = int(input());
divisors = [i for i in range(1,n) if n % i==0];
if sum(divisors) < n:
	print("Deficient");
else:
	print("Not deficient");