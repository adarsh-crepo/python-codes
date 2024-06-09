print ("Welcome to Burger Shop!")
burgerSize=input(" What size Burger do you want? M, N or L: ")
addMashroom=input("Do you want mashroom? Y or N: ")
extraCheese=input("Do you want extra cheese? Y or N: ")

bill=0

if burgerSize==M:
    bill +=5
elif burgerSize==N:
    bill +=8
elif burgerSize==L:
    bill += 10

if addMashroom == "Y":
    if burgerSize == "L":
        bill += 2
    else:
        bill += 1

if extraCheese == "Y":
    bill += 1

print (f"Your final bill is: {bill}.")