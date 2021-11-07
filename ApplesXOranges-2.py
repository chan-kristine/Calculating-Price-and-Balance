def Show_Prices():
    price_A = 20
    price_O = 25
    print(f"The price of an apple is {price_A} pesos.")
    print(f"The price of an orange is {price_O} pesos.")
    return price_A, price_O

def Get_the_Quantities():
    ApplesQuantity = int(input("How many apples will you buy? "))
    OrangesQuantity = int(input("How many oranges will you buy? "))
    return ApplesQuantity, OrangesQuantity

def Total_Price(price_A, price_O, ApplesQuantity, OrangesQuantity):
    Apple_TP = price_A * ApplesQuantity
    Orange_TP = price_O * OrangesQuantity
    Total_Price = Apple_TP + Orange_TP
    return Total_Price

def display(solve):
    print(f"The total amount is {solve} pesos.")
# steps
# 1. show the price of an apple and an orange
PriceA, PriceO = Show_Prices()
# 2. ask how many apples and oranges will they buy
AmountA, AmountO = Get_the_Quantities()
# 3. solve for the total price
solve = Total_Price(PriceA, PriceO, AmountA, AmountO)
# 4. display the total price
display(solve)