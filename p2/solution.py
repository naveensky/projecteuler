limit = 4000000
# limit = 90
prev = 1
current = 2
sum = 0

while (current<limit):
    if(current%2==0):
        sum = sum + current
    
    temp = current
    current = current + prev
    prev = temp
      
print "The sum is {0}".format(sum)