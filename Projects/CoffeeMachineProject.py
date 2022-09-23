# Coffee variables
water = 300
milk = 200
coffee = 100
money = 0.0
# Coin variables
totalCoinValue = 0.0
quarters = 0.0
dimes = 0.0
nickles = 0.0
pennies = 0.0
cost = 0.0
waterUsage = 0
milkUsage = 0
coffeeUsage = 0
refund = 0.0
# While loop constraint
i = 0


def report():
    print("Water:  " + str(water) + "ml\n"
          + "Milk:   " + str(milk) + "ml\n"
          + "Coffee: " + str(coffee) + "ml\n"
          + "Money:  $" + str(money))


def insertCoins():
    global money

    quarters = (float(input("How many quarters?: ")) * .25)
    dimes = (float(input("How many dimes?: ")) * .1)
    nickles = (float(input("How many nickles?: ")) * .05)
    pennies = (float(input("How many pennies?: ")) * .01)
    totalCoinValue = quarters + dimes + nickles + pennies

    if totalCoinValue - cost > 0.0:
        refund = round(totalCoinValue - cost, 2)
        print("Here is $" + str(refund) + " dollars in change.")
        money = + cost

    elif totalCoinValue - cost == 0.0:
        print("No change")

    elif totalCoinValue - cost < 0.0:
        print("Sorry that's not enough money.")


def resourceChecker():
    global water
    global coffee
    global milk

    if water >= waterUsage:
        if coffee >= coffeeUsage:
            if milk >= milkUsage:
                water = water - waterUsage
                coffee = coffee - coffeeUsage
                milk = milk - milkUsage
                insertCoins()

            else:
                print("Not enough milk")
        else:
            print("Not enough coffee")
    else:
        print("Not enough water")


# Instructions
print("Enter 'report' to print resources available and 'off' to exit")


# Enter loop for choosing coffee
while i != 1:
    # Ask user what they want(off exits and report prints resources).
    val = input("What would you like? (espresso/latte/cappuccino): ")

    if val == "report":
        report()

    elif val == "espresso":
        cost = 1.5
        waterUsage = 50
        coffeeUsage = 18
        milkUsage = 0
        resourceChecker()

    elif val == "latte":
        cost = 2.5
        waterUsage = 200
        coffeeUsage = 24
        milkUsage = 150
        resourceChecker()

    elif val == "cappuccino":
        cost = 3.0
        waterUsage = 250
        coffeeUsage = 24
        milkUsage = 100
        resourceChecker()

    elif val == "off":
        exit()
