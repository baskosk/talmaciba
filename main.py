MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money=0.0
value=0.0
change=0.0
price=0.0
COINS = [
    {
        "Penny": "1 cent",
        "cost": 0.01
    },
    {
        "Nickel": "5 cents",
        "cost": 0.05
    },
    {
        "Dime": "10 cents",
        "cost": 0.1
    },
    {
        "Quarter": "25 cents",
        "cost": 0.25
    }
]


#Turns on/off machine
turn_on=True

while turn_on:
    #TODO: Makes report command about water, milk, coffee and money quantity in coffee machine
    #TODO: Makes program what choose coffee between espresso/late/cappuccino
    command=input("What would you like? (espresso/latte/cappuccino)").lower()
    if command in MENU:
        # Get required ingredients
        ingredients = MENU[command]["ingredients"]

        # Check if there are enough resources
        can_make = True
        for item in ingredients:
            if resources[item] < ingredients[item]:
                print(f"Sorry, there is not enough {item}.")
                can_make = False
                break


        # If enough resources, make the coffee
        if can_make:
            print(f"The price is: {MENU[command]['cost']}")
            print("Please insert coins.")
            # TODO: Input quarters, dimes, nickels and pennies and count total value and change.
            # TODO: Makes programs what counts coins quantity and value.
            while value<MENU[command]["cost"]:
                quarters = float(input("How many quarters?"))
                value += quarters * 0.25
                print(f"Total inserted:{value}")
                if value>=MENU[command]["cost"]:
                    change=value-MENU[command]["cost"]
                    value=0
                    print(f"Here is your change:{change}")
                    price = MENU[command]["cost"]
                    break
                dimes = float(input("How many dimes?"))
                value += dimes * 0.1
                print(f"Total inserted:{value}")
                if value>=MENU[command]["cost"]:
                    change=value-MENU[command]["cost"]
                    value=0
                    print(f"Here is your change:{change}")
                    price = MENU[command]["cost"]
                    break
                nickels = float(input("How many nickels?"))
                value += nickels * 0.05
                print(f"Total inserted:{value}")
                if value>=MENU[command]["cost"]:
                    change=value-MENU[command]["cost"]
                    value=0
                    print(f"Here is your change:{change}")
                    price = MENU[command]["cost"]
                    break
                pennies = float(input("How many pennies?"))
                value += pennies * 0.01
                if value>=MENU[command]["cost"]:
                    change=value-MENU[command]["cost"]
                    value=0
                    print(f"Here is your change:{change}")
                    price=MENU[command]["cost"]
                    break
                else:
                    print("Not enough money")
                    change=value
                    value=0
                    print(f"Here is your change:{change}")
                    price=0
                    break

            money += price
            for item in ingredients:
                resources[item] -= ingredients[item]  # Deduct resources
            # TODO: Makes coffee
            print(f"Here is your {command}! ☕ Enjoy!")

    elif command == "report":
        #Machine report
        print("\n📋 Machine Report:")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"💰 Money: ${money:.2f}")

    elif command == "off":
        print("Turning off the coffee machine... ☕")
        turn_on=False
    else:
        print("Invalid choice. Please select a valid coffee option.")







