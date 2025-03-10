snackchoice = input("What kind of snack do you want? It can be sweet or salty.").lower()
drinkchoice = input("What kind of drink do you want: soda, juice, or water?").lower()

if "sweet" in snackchoice and "soda" in drinkchoice:
    print("I recommend chocolate and soda.")

elif "salty" in snackchoice or "juice" in drinkchoice:
    print ("You should try pretzels and juice.")
    
elif "water" in drinkchoice:
    print("Water and fresh fruit is a good option.")

else:
    print("You should choose your favorite drink and snack.")
