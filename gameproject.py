import random
import time
import sys

Dice = random.randint(1, 12)
Dice2 = random.randint(1, 6)
Dice3 = random.randint(1, 6)
Dice4 = random.randint(1, 12)
DoubleDice = ((Dice + Dice2)*2)
DoubleDice2 = ((Dice3 + Dice4)*2)
Score1 = (Dice + Dice2)
Score2 = (Dice3 + Dice4)
def DiceRoll(Dice, Dice2, Dice3, Dice4):
	Dice = random.randint(1, 12)
	Dice2 = random.randint(1, 6)
	Dice3 = random.randint(1, 12)
	Dice4 = random.randint(1, 6)
	DoubleDice = ((Dice + Dice2)*2)
	DoubleDice2 = ((Dice3 + Dice4)*2)
	Score1 = (Dice + Dice2)
	Score2 = (Dice3 + Dice4)
	print("Player 1, Roll?")
	Roll = input("Y/N?")
	if Roll =="y":
		print("Ok!")
	if Roll == "n":
		print("Goodbye!")
		time.sleep(2)
		sys.exit(0)
	print(Dice, Dice2)
	Score1 = (Dice + Dice2)
	print(Score1)
	if Dice == Dice2:
		Score1 = DoubleDice
		DoubleDice = ((Dice + Dice2)*2)
		print(DoubleDice)
	
	
	print("Player 2, Roll?")
	Roll2 = input("Y/N?")
	if  Roll2 =="y":
		print("Ok!")
	if Roll2 == "n":
		print("Goodbye!")
		time.sleep(2)
		sys.exit(0)
	print(Dice3, Dice4)
	Score2 = (Dice3 + Dice4)
	print(Score2)
	if Dice3 == Dice4:
		Score2 = DoubleDice2
		DoubleDice2 = ((Dice3 + Dice4)*2)
		print(DoubleDice2)
	if Score1 > Score2:
		print("Player 1:", Score1, "Player 2:", Score2)
		print("Player 1 Wins!")
	if Score1 < Score2:
		print("Player 1:", Score1, "Player 2:", Score2)
		print("Player 2 Wins!")
	if Score1 == Score2:
		print("Player 1:", Score1, "Player 2:", Score2)
		print("Tie!")
	
	
	

print(""" ____  _____  __    __      ____  _   _  ____    ____  ____  ___  ____ 
(  _ \(  _  )(  )  (  )    (_  _)( )_( )( ___)  (  _ \(_  _)/ __)( ___)
 )   / )(_)(  )(__  )(__     )(   ) _ (  )__)    )(_) )_)(_( (__  )__) 
(_)\_)(_____)(____)(____)   (__) (_) (_)(____)  (____/(____)\___)(____)""")		
print("Would you like to play dice?")
Dice = input ("Y/N?")
if Dice == "n":
	print("Goodbye!")
	time.sleep(2)
	sys.exit(0)
elif Dice =="y":
	print("Let's play!")
	
DiceRoll(Dice, Dice2, Dice3, Dice4)