print("""Min 2 players
each player should have a set of dice
dice should be of multiple types
players should roll dice against each other
players win or lose based on rules you decide""")

print("""Bonus
AI player
persistent high score""")

import random
import sys
import time


def DiceRoll():
	DiceRoll = random.randint(0,12)
	DiceRoll2 = random.randint(0,12)
	print(DiceRoll, DiceRoll2)
	if DiceRoll == DiceRoll2:
		print((DiceRoll) * 2)
	

print("Would you like to play dice?")
Dice = input ("Y/N?")
if Dice == "n":
	print("Goodbye!")
elif Dice =="y":
	print("Let's play!")
	
print("Player 1, Roll?")
Roll = input("Y/N?")
while  Roll =="y":
	DiceRoll()
	break
if Roll == "n":
	print("Goodbye!")
	time.sleep(2)
	sys.exit(0)


print("Player 2, Roll?")
Roll = input("Y/N?")
while  Roll =="y":
	DiceRoll()
	break
if Roll == "n":
	print("Goodbye!")
	time.sleep(2)
	sys.exit(0)
	
	






