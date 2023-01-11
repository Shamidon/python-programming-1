def fib(n):
	if n <= 1:
		return n
	return fib(n-1) + fib(n-2)
def countWays(s):
	return fib(s + 1)
s=int(input("ENTER NO.OF.STEPS: "))
print ("NUMBER OF WAYS = ",countWays(s))

