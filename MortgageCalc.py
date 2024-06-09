try:

    salary = int(input("What is your salary?"))
except:
    print("There was an error")

else:
    if salary > 2000:
        print("You are elligible")
    else: 
        print("Sorry! you are not elligible")

finally:
    print("Thanks for using our calculater")