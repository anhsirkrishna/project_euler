limit = 1000
n=3
sum=0
while(n<limit):
	if(n%5==0):
		n = n + 3
		continue

	sum = sum + n
	n = n + 3
n=5
while(n<limit):
	sum = sum + n
	n = n + 5
	
print("The sum is : ", sum)