resources = {
"Water": 100,
"Milk" : 100,
"Coffee" : 76,
"Money" : 1
}
running = True
while running:
    prompt = input("What would you like? (espresso/latte/capuccino)\n").lower()
    progress = True
    if prompt == "report":
        print(resources)
    if prompt == "espresso":
        resources["Water"] -= 50
        resources["Milk"] -= 10
        resources["Coffee"] -= 10
        resources["Money"] += 10
        for resource in resources:
            if resources[resource] < 0:
                print(f"Sorry there is not enough {resource.lower()}")
                progress = False
        if progress:
            quaters = int(input("How many quaters?"))
            dimes = int(input("How many dimes?"))
            nickles = int(input("How many nickles?"))
            pennies = int(input("How many pennies?"))
            total = quaters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

            if total >= 10:
                change = total - 10
                print(f"Your change is {change}")
            else:
                print("You do not have enough money")
                resources["Water"] += 50
                resources["Milk"] += 10
                resources["Coffee"] += 10
                resources["Money"] -= 10
