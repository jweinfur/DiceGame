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
	Dice = random.randint(0,12)
	Dice2 = random.randint(0,6)
	print(Dice, Dice2)
	if Dice == Dice2:
		print((Dice) * 2)
	else:
		print(Dice + Dice2)
def DiceRoll2():
	Dice3 = random.randint(0,12)
	Dice4 = random.randint(0,6)
	print(Dice3, Dice4)
	if Dice3 == Dice4:
		print((Dice3) * 2)
	else:
		print(Dice3 + Dice4)

	
print("Would you like to play dice?")
Dice = input ("Y/N?")
if Dice == "n":
	print("Goodbye!")
	time.sleep(2)
	sys.exit(0)
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
	DiceRoll2()
	break
if Roll == "n":
	print("Goodbye!")
	time.sleep(2)
	sys.exit(0)

if DiceRoll > DiceRoll2:
	print("Player 1 Wins!")
elif DiceRoll2 > DiceRoll:
	print("Player 2 Wins!")
	



	
	






