# Coffee Shop Simulator

# imports.
import random

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
    for _ in range(x):
        numList.append(y)
    return numList

class CoffeeShopSim:

    TEMPMIN = 20
    TEMPMAX = 90

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
            temp = self.weather()

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

    def simulate(self, temp, advertising, cupPrice):
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
            distFromMaxDist = maxDistFromAvg - distFromAvg

            # If the value is zero, change it to 1.
            if distFromMaxDist == 0:
                distFromMaxDist = 1
            # Add the output from xOFy to the temps list.
            for t in xOFy(int(distFromMaxDist), i):
                temps.append(t)
        return temps
    
    def incDay(self):
        self.day += 1

    def dailyStats(self, temp):
        print(f'You have ${self.cash:.2f} cash on hand and the temperature is {temp} degrees.')
        print(f'You have enough coffee on hand to make {self.coffeeInv} cups of coffee.\n')

    def dayHeader(self):
        print(f'\n-----| Day {self.day} at {self.shopName} |-----')
    
    def dailySales(self, temp, advertising):
        return int((self.TEMPMAX - temp) * (advertising * 0.5))
    
    def weather(self):
        return random.choice(self.temps)

welcome()
playerName = prompt("What is your name? ")
playerShop = prompt("What is the name of your coffee shop? ")

game = CoffeeShopSim(playerName, playerShop)

game.run()