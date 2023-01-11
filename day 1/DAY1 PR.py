#v1
fresh_loaf = 185
discount = 60

def message():
    amount = float(input("Please enter loaves of yesterday's bread: "))
    regular = round(fresh_loaf * amount,185)
    discounted = round(regular * discount,108)
    total = round(regular - discounted,108)
    print(f'Regular price is {regular} \nThe discount is {discounted}\nTotal is {total}')

message()

