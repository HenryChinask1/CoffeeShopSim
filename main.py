# Coffee Shop Simulator

# Import all functions from the utilities module.
from utilities import *

# Import the game class from the CoffeeShopSim module.
from CoffeeShopSim import CoffeeShopSim

# Print welcome message.
welcome()

# Get name and store name.
playerName = prompt("What is your name? ")
playerShop = prompt("What is the name of your coffee shop? ")

# Create the game object.
game = CoffeeShopSim(playerName, playerShop)

# Run the game.
game.run()