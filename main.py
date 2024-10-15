print("Select your ride:")
print("1. BIKE")
print("2. CAR")
choice = int(input("Enter choice"))
if (choice == 1):
    print("Type of bike:")
    print("1. Bike\n")
    print("2. Scooty\n")
    choice2 = int(input("Enter your choice 2:"))
    if choice2 == 1:
        print("You selected bike")
    else:
        print("You seleceted scooty")
elif (choice == 2):
    print("Which car?")
    print("1. Sedan")
    print("2. SUV")
    choice3 = int(input("Enter your choice 2:"))
    if choice3 == 1:
        print("You chose sedan")
    else:
        print("You chose SUV")
else:
    print("Wrong choice")


