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
	DoubleDice2 = (((Dice1 + Dice3)*2) + Dice2)
	DoubleDice3 = (((Dice2 + Dice3)*2) + Dice1)
	DoubleDice4 = (((Dice4 + Dice5)*2) + Dice6)
	DoubleDice5 = (((Dice4 + Dice6)*2) + Dice5)
	DoubleDice6 = (((Dice5 + Dice6)*2) + Dice4)
	TripleDice1 = ((Dice1 + Dice2 +Dice3) * 3)
	TripleDice2 = ((Dice4 + Dice5 +Dice6) * 3)
	
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
		Score1 = DoubleDice1
		print(Score1)
	if Dice1 ==Dice3:
		Score1 = DoubleDice2
		print(Score1)
	if Dice2 == Dice3:
		Score1 = DoubleDice3
		print(Score1)
	if Dice1 == Dice2 ==Dice3:
		Score1 = TripleDice1
		print(Score1)
	print("""	
			""")
	
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
		Score2 = DoubleDice4
		print(Score2)
	if Dice4 == Dice6:
		Score2 = DoubleDice5
		print(Score2)
	if Dice5 == Dice6:
		Score2 = DoubleDice6
		print(Score2)
	if Dice4 == Dice5 ==Dice6:
		Score2 = TripleDice2
		print(Score2)
	print("""	
			""")
	if Score1 > Score2:
		print("Player 1:", Score1, "Player 2:", Score2)
		print("Player 1 Wins!")
	if Score1 < Score2:
		print("Player 1:", Score1, "Player 2:", Score2)
		print("Player 2 Wins!")
	if Score1 == Score2:
		print("Player 1:", Score1, "Player 2:", Score2)
		print("Tie!")
	
	

print("""                  d8,           d8b                  d8b   d8,              
   d8P            `8P            88P                  88P  `8P               
d888888P                        d88                  d88                     
  ?88'    88bd88b  88b?88,.d88b,888   d8888b     d888888    88b d8888b d8888b
  88P     88P'  `  88P`?88'  ?88?88  d8b_,dP    d8P' ?88    88Pd8P' `Pd8b_,dP
  88b    d88      d88   88b  d8P 88b 88b        88b  ,88b  d88 88b    88b    
  `?8b  d88'     d88'   888888P'  88b`?888P'    `?88P'`88bd88' `?888P'`?888P'
                        88P'                                                 
                       d88                                                   
                       ?8P             """)
print("""	
				""")
		
print("Would you like to roll the dice?")
Dice = input ("Y/N?")
if Dice == "n":
	print("Goodbye!")
	time.sleep(1)
	sys.exit(0)
elif Dice =="y":
	print("Let's play!")
	time.sleep(1)
print("""	
			""")
	
print("""Rules:
1. Each player rolls 3 dice. One 20-sided die, one 12-sided die, and one 6-sided die
2. Total the score by adding all the dice together
3. If a player rolls two of the same number, add those two dice together and
 multiply by 2 and then add the third die to the total
4. Player with the highest score wins""")
print("""	
			""")
DiceRoll()
print("""	
			""")


while True:
	print("""	
			""")
	print("Would you like to play again?")
	Replay = input("Y/N?")
	if Replay == "y":
		print("""	
			""")
		DiceRoll()
		continue
	if Replay == "n":
		print("Goodbye!")
		time.sleep(2)
		sys.exit(0)