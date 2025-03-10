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

def checkForEnoughCash(cash: float, purchase: float) -> float:
    if cash - purchase >= 0:
        return cash - purchase
    else:
        print(f'You do not have enough cash for the purchase {cash} dollars on hand.')
        return cash