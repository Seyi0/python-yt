import sys
import random
from enum import Enum

class RPS (Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3



#print an empty line
print("")
playerchoice = input("Enter ...\n1 for Rock, \n2 for Paper, \n3 for scissors:\n\n")


player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

# note : two if statement can't follow each other use "elif" instead....
if player == 1 and computer == 3:
    print("You won😎")
elif player == 2 and computer == 1:
    print("You won😎")
elif player == 3 and computer == 2:
    print("You won😎")
elif player == computer:
    print("draw👀")
else:
    print("python won😢")