from datetime import datetime, timedelta;
#Dictionary used for mapping the days with integer values
days = {	"Saturday": 1,"Sunday": 2,"Monday": 3,"Tuesday": 4,"Wednesday": 5,"Thursday": 6,"Friday": 7} 
gday = str(input()).rstrip();
h = int(input());
m = int(input());
#using the datetime class to create an object with the specified time
gmt = datetime(2016, 10, days[gday], h, m);
#using timedelta class we can just add up time
difference = timedelta(hours=5, minutes=30); 
ist = gmt + difference;
iday = ist.day % 7;
#just finding the key for the particular value we got (iday)
l = [print(x) for x,y in days.items() if y == ist.day]
print(ist.hour);
print(ist.minute);

