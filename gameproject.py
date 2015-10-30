print("""Min 2 players
each player should have a set of dice
dice should be of multiple types
players should roll dice against each other
players win or lose based on rules you decide""")

print("""Bonus
AI player
persistent high score""")


print("Would you like to play dice?")
Dice = input ("Y/N?")
if Dice == "n":
	print("Goodbye!")
elif Dice =="y":
	print("Let's play!")
	
while Dice =="y":
	print("Roll")
	if Dice == "n":
		print("Goodbye!")
	break
