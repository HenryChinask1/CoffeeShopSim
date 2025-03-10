# Coffee Shop Simulator

# imports.
import random
import re
from utilities import *

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
            self.cash = checkForEnoughCash(self.cash, advertising)

            # Offer to purchase coffee inventory,
            print(f'You have {self.coffeeInv} units of coffee on hand.')
            coffeePurchase = float(prompt('How much coffee do you want to purchase? (0 for None)', False))
            coffeePurchase = convertToFloat(coffeePurchase)
            self.cash = checkForEnoughCash(self.cash, coffeePurchase)

            # Simulate the sales for the day.
            cupsSold = self.simulate(temp, advertising, cupPrice, self.coffeeInv)
            grossProfit = cupsSold * cupPrice

            # Display the results.
            print(f'\nYou sold {cupsSold} cups of coffee today.')
            print(f'You made ${grossProfit}.')
            self.cash += grossProfit
            self.coffeeInv -= cupsSold
            self.incDay()

            # Offer an exit to the game.
            quit = prompt('Would you like to continue selling coffee? (press any key or press Q to quit game)')
            if quit.lower() == 'q':
                running = False

    def simulate(self, temp, advertising, cupPrice, coffeeInv):
        # Calculate cups sold.
        cupsSold = self.dailySales(temp, advertising, coffeeInv)

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
    
    def dailySales(self, temp, advertising, coffeeInv):
        if coffeeInv - int((self.TEMPMAX - temp) * (advertising * 0.5)) < 0:
            return coffeeInv
        return int((self.TEMPMAX - temp) * (advertising * 0.5))
    
    def weather(self):
        return random.choice(self.temps)