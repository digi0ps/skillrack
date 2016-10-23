x,y,s,e = [int(input()) for i in range(4)];
hpd = e+12-s; #Hours per day
tpd = hpd/y; #Tablets per day
days = x/tpd;
print(round(days)-1)