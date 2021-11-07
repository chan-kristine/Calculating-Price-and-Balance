def getNameAgeAddress():
    name_ = input("Name: ")
    age_= int(input("Age: "))
    add_= input("Address: ")
    return name_, age_, add_

def display(nameF, ageF, addF):
    print(f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addF}.")


name, age, add = getNameAgeAddress()


display(name, age, add)