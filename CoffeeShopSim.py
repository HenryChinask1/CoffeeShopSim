# Coffee Shop Simulator

# imports.
import random

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

def welcome() -> str:
    print('Welcome to the Coffee Shop Simulator.')
    print('Version 1')
    print("Let's collect some information before we start.\n")

def prompt(display='Please enter a response', require=True) -> str:
    if require:
        userField = False
        while not userField:
            userField = input(display + ' ')
    else:
        userField = input(display + ' ')
    return userField

def convertToFloat(num: int) -> float:
    # If the conversion fails, make it zero (0).
    try:
        num = float(num)
    except ValueError:
        return 0
    return num

def xOFy(x: int, y: int) -> list:
    numList = []
    for i in range(x):
        numList.append(y)
    return numList

class CoffeeShopSim:

    def __init__(self, playerName, shopName):
        self.playerName = playerName
        self.shopName = shopName
        self.day = 1
        self.cash = 100.00
        self.coffeeInv = 100
        self.sales = []
        self.temps = self.setTemps()
    
    def run(self):
        print("\nLet's get started!\n")
    
        running = True
        while running:
            # Display the day with a fancy header.
            self.dayHeader()

            # Get the weather for the day.
            temp = self.weather

            # Display the cash and the weather.
            self.dailyStats(temp)

            # Get the price of a cup of coffee.
            cupPrice = float(prompt("What do you want to charge for a cup of coffee? "))

            # Get the advertising spend.
            print('\nYou can buy advertising to help boost sales.')
            advertising = float(prompt("How much do you want to spend on advertising? (0 for None) ", False))
            advertising = convertToFloat(advertising)
            self.cash -= advertising

            # Simulate the sales for the day.
            cupsSold = self.simulate(temp, advertising, cupPrice)
            grossProfit = cupsSold * cupPrice

            # Display the results.
            print(f'\nYou sold {cupsSold} cups of coffee today.')
            print(f'You made ${grossProfit}.')
            self.cash += grossProfit
            self.coffeeInv -= cupsSold
            self.incDay()

    def siumulate(self, temp, advertising, cupPrice):
        # Calculate cups sold.
        cupsSold = self.dailySales(temp, advertising)

        # Save the sales results for the day.
        self.sales.append({"day": self.day,
                           'coffeeInv': self.coffeeInv,
                           'advertising': advertising,
                           'temperature': temp,
                           'cupPrice': cupPrice,
                           'cupsSold': cupsSold})
        return cupsSold
    
    def setTemps(self):
        temps = []

        avg = (self.TEMPMIN + self.TEMPMAX) / 2
        maxDistFromAvg = self.TEMPMAX - avg

        for i in range(self.TEMPMIN, self.TEMPMAX):
            distFromAvg = abs(avg - i)

def dailyStats(cashOnHand, weather, coffeeInv):
    print(f'You have ${cashOnHand:.2f} cash on hand and the temperature is {weather} degrees.')
    print(f'You have enough coffee on hand to make {coffeeInv} cups of coffee.\n')

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
