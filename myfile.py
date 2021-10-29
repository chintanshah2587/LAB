import sys
num = len(sys.argv)
def getSum(num):
sum = 0
for i in range(1,num):
for digit in str(sys.argv[i]):
sum+=int(digit)
return sum
print(getSum(num))
