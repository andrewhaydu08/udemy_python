name = input("please tell me your name:")
sales = input("please tell me your total month sales:")
"these will be stored variables"

"turns you sales into integers"
sales = int(sales)
commission = sales * 13 / 100
commission = round(commission, 2)
print(f"Hello {name}, your commission this month is ${commission}")

