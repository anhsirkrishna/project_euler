n = 1
m = 2
x = n + m
sum = 2
while(x<4000000):
	x=n+m
	print(x)
	if(not(x & 1)):
		print(x)
		sum = sum + x
	n=m
	m=x
	
print(sum)