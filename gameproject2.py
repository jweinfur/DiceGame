import random
import time
import sys


def DiceRoll():
	Dice = random.randint(0,12)
	Dice2 = random.randint(0,6)
	Dice3 = random.randint(0,12)
	Dice4 = random.randint(0,6)
	print("Player 1, Roll?")
	Roll = input("Y/N?")
	if Roll =="y":
		print("Ok!")
	if Roll == "n":
		print("Goodbye!")
		time.sleep(2)
		sys.exit(0)
	print(Dice, Dice2)
	if Dice == Dice2:
		print((Dice) * 2)
	else:
		print(Dice + Dice2)

	print("Player 2, Roll?")
	Roll2 = input("Y/N?")
	if  Roll2 =="y":
		print("Ok!")
	if Roll2 == "n":
		print("Goodbye!")
		time.sleep(2)
		sys.exit(0)
	print(Dice3, Dice4)
	if Dice3 == Dice4:
		print((Dice3) * 2)
	else:
		print(Dice3 + Dice4)
		
	if (Dice + Dice2) > (Dice3 +Dice4):
		print("Player 1:", Dice + Dice2, "Player 2:", Dice3+Dice4)
		print("Player 1 Wins!")
	if (Dice3 +Dice4) > (Dice + Dice2):
		print("Player 1:", Dice + Dice2, "Player 2:", Dice3+Dice4)
		print("Player 2 Wins!")
	if (Dice + Dice2) == (Dice3 + Dice4):
		print("Player 1:", Dice + Dice2, "Player 2:", Dice3+Dice4)
		print("Tie!")

print("Would you like to play dice?")
Dice = input ("Y/N?")
if Dice == "n":
	print("Goodbye!")
	time.sleep(2)
	sys.exit(0)
elif Dice =="y":
	print("Let's play!")
	
DiceRoll()