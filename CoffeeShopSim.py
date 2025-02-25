# Coffee Shop Simulator

import random

day = 1

cash = 100.00

coffee = 100

# Sales list of Dictionaries
# sales = [
#     {
#         'day': 1,
#         'coffeeInv': 100,
#         'advertising': '10',
#         'temp': 69
#         'cupsSold': 16
#     },
#     {
#         'day': 2,
#         'coffeeInv': 84,
#         'advertising': '15',
#         'temp': 72,
#         'cupsSold': 20
#     },
#     {
#         'day': 2,
#         'coffeeInv': 64,
#         'advertising': '5',
#         'temp': 78,
#         'cupsSold': 10
#     }
#     ]
# Create an empty sales list.
sales = []
def welcome():
    print('Welcome to the Coffee Shop Simulator.')
    print('Version 1')
    print("Let's collect some information before we start.\n")

def prompt(display='Please enter a response', require=True):
    if require:
        userField = False
        while not userField:
            userField = input(display + ' ')
    else:
        userField = input(display + ' ')
    return userField

def dailyStats(cashOnHand, weather, coffeeInv):
    print(f'You have ${cashOnHand:.2f} cash on hand and the temperature is {weather} degrees.')
    print(f'You have enough coffee on hand to make {coffeeInv} cups of coffee.\n')

def convertToFloat(num):
    # If the conversion fails, make it zero (0).
    try:
        num = float(num)
    except ValueError:
        return 0
    return num

def getWeather():
    # Generate a random temp between 20 and 90.
    return random.randint(20, 91)

# Print welcome message.
welcome()

# Get name and store name.
name = prompt('Enter your name.\n')
storeName = prompt('Enter the name of your coffee shop.\n')

print("Ok, let's get started!")

# Main game loop.
running = True
while running:
    # Display the day with a text effect.
    print(f'\n-----| Day {day} at {storeName} |-----')
    temp = getWeather()

    # Display cash and weather.
    dailyStats(cash, temp, coffee)

    # Get price of a cup of coffee.
    cupPrice = prompt('What will you charge for a cup of coffee? ')

    # Get advertising budget.
    print('\nYou can buy advertising to help promote sales.')
    advertising = convertToFloat(prompt("How much do you want to spend on advertising? (0 for none) ", False))

    cash -= advertising

    # TODO: Calculate the day's stats.
    # TODO: Display the day's stats.

    # Move to next day.
    day += 1
