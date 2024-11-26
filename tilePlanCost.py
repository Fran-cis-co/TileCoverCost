from decimal import Decimal # import Decimal to allow the user to input numbers with a decimal
from utility.area import findArea

# Function which will call in everything to determine the cost of the floor tile plan
def determineCost(width, height, tileCost):
    area = findArea(width, height)
    print("Your cost will be: $", area * tileCost)

# Function which will ask the user the width, height, and cost per square foot
def askUser():
    print("Hello! \n")

    # Grab width, height, and cost of the tile cover from the user to calculate the cost to cover an entire floor
    width = Decimal(input("Please input the width: \n"))
    height = Decimal(input("Please input the height: \n"))
    tileCost = Decimal(input("Please input the cost per square foot: \n"))

    determineCost(width, height, tileCost)
