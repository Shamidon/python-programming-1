
def checkleapyr(year):
    if year%400==0 or year%4==0:
        print(year," IS A LEAP YEAR")
    else:
        checkleapyr(year-1)
try:
    yr = int(input("ENTER THE YEAR: "))
    if yr > 0:
        checkleapyr(yr)
    else:
        print("YEARS CAN'T BE NEGATIVE...! OR ZERO...!")
except :
    print("WRONG VALUE")
