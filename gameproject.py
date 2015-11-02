import random
import time
import sys


def DiceRoll():
	Dice1 = random.randint(1, 20)
	Dice2 = random.randint(1, 12)
	Dice3 = random.randint(1,6)
	Dice4 = random.randint(1, 20)
	Dice5 = random.randint(1, 12)
	Dice6 = random.randint (1, 6)
	DoubleDice1 = (((Dice1 + Dice2)*2) + Dice3)
	DoubleDice2 = (((Dice4 + Dice5)*2) + Dice6)
	TripleDice1 = ((Dice1 + Dice2 +Dice3) * 3)
	TripleDice2 = ((Dice4 + Dice5 +Dice6) * 3)
	Score1 = (Dice1 + Dice2)
	Score2 = (Dice3 + Dice4)
	print("Player 1, Roll?")
	Roll = input("Y/N?")
	if Roll =="y":
		print("Ok!")
	if Roll == "n":
		print("Goodbye!")
		time.sleep(2)
		sys.exit(0)
	print(Dice1, Dice2, Dice3)
	Score1 = (Dice1 + Dice2 + Dice3)
	print(Score1)
	if Dice1 == Dice2:
		Score1 = DoubleDice
		print(Score1)
	if Dice1 == Dice2 ==Dice3:
		Score1 = TripleDice1
		print(Score1)
	
	
	print("Player 2, Roll?")
	Roll2 = input("Y/N?")
	if  Roll2 =="y":
		print("Ok!")
	if Roll2 == "n":
		print("Goodbye!")
		time.sleep(2)
		sys.exit(0)
	print(Dice4, Dice5, Dice6)
	Score2 = (Dice4 + Dice5 + Dice6)
	print(Score2)
	if Dice4 == Dice5:
		Score2 = DoubleDice2
		print(Score2)
	if Dice4 == Dice5 ==Dice6:
		Score2 = TripleDice2
		print(Score2)
	
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
	
DiceRoll()