MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

coins=[
    ("quarters", 0.25),
    ("dimes" , 0.10),
    ("nickles" , 0.05),
    ("pennies" , 0.01)
]

money = 0
isRun=True

def printReport():
    print(f"Water : {resources["water"]}ml")
    print(f"Milk : {resources["milk"]}ml")
    print(f"Coffee : {resources["coffee"]}g")
    print(f"Money : ${money}")

while isRun:
    order=input("what would you like? (espresso/latte/cappuccino) : ").lower()

    # TODO : 1. Print what would you like? (espresso/latte/cappuccino)
        # 1.1 : if input is "off" close the console
        # 1.2 : if input is "reports" print the all resources

    if order == 'off':
        isRun=False
    elif order == 'reports':
        printReport()
    else :
        flag=True
        # TODO : 2. check the resources , we can make drink?
            # 2.1 : 만약 부족하다면 sorry
            # 2.2 : 부족 하지 않다면 3번으로
        for key in MENU[order]['ingredients'].keys():
            if MENU[order]['ingredients'][key]>resources[key]:
                flag=False
                print(f"Sorry there is not enough {resources[key]}")

        if flag:
            input_coins=0

            for i in range(len(coins)):
                input_coins+=int(input(f"{coins[i][0]} : "))*coins[i][1]

            input_coins-=MENU[order]['cost']
            if input_coins<0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if input_coins>0:
                    print("Here is $%.2f dollars in change."%input_coins)

                print("E.g. report before purchasing latte:")
                printReport()
                print()

                for key in MENU[order]['ingredients'].keys():
                    resources[key]-=MENU[order]['ingredients'][key]

                money+=MENU[order]['cost']

                print("E.g. report after purchasing latte:")
                printReport()
                print()

                print(f"Here is your {order}. Enjoy!")



# TODO : 3. customer inputs there money
# 3.1 : 돈이 부족하다면 실패후 돈 돌려줘
# 3.2 : 정상 입력 되었다면 돈 받고 거스름돈 돌려주고 커피 줘라

