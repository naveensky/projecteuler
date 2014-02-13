sum = 0

for n in range(1, 1000):
	if(n%5==0 and n%3 ==0):
		sum = sum + n
	elif(n%3==0 or n%5 ==0):
		sum = sum + n
	
print "The sum is {0}".format(sum)