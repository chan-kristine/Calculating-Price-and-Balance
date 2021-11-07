def Get_init_info():
    amount_of_Money = int(input("Please enter your current money balance: "))
    price_of_Apple = int(input("Please enter the price of an apple: "))
    return amount_of_Money, price_of_Apple

def Show_the_Result(amount_money, ApplePrice):
    Maximum_Apples = amount_money // ApplePrice
    Change_ = amount_money % ApplePrice
    return Maximum_Apples, Change_

def Display(Maximum_Apples, Change_):
    print(f"You can buy {Maximum_Apples} apples and your change is {Change_} pesos.")


amount_money, ApplePrice = Get_init_info()

Maximum_Apples, Change_ = Show_the_Result(amount_money, ApplePrice)

Display(Maximum_Apples, Change_)