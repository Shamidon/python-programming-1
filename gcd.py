def findGreatestCD(a, b):
    if(b == 0):
        return a;
    else:
        return findGreatestCD(b, a % b)
    
num1 = float(input(" Please Enter the First Value  : "))
num2 = float(input(" Please Enter the Second Value : "))

Val = findGreatestCD(num1, num2)
print("\n The Result of" ,num1 ,"and" ,num2,"=",Val)
