import random
#initialization
#choose number of matches
print("""Let`s play a game. We take turns removing flags.
You want to be the one that removes the last flag. 
The twist is that on each turn you must remove 1, 2, or 3 flags. 
You can choose the number of matches. Good luck!""")
giveusnumber = True
while giveusnumber:
    try:
        numberOfMatches = int(input("Enter number of matches. Choose number bigger than 10 for that game.\n"))
        if numberOfMatches > 10:
            giveusnumber = False
    except:
        giveusnumber = True
# choose who is first
activePlayer = input("""Now choose who will start the game: player or computer:
Enter p if player, enter c if computer\n""")
while not (activePlayer == "c" or activePlayer == "p"):
    activePlayer = input("Enter p or c\n")
#game
def turn(activePlayer, numberOfMatches):
    if activePlayer == "p":
        print(numberOfMatches * "I")
        inputNumber = int(input("Enter number of matches to delete: 1, 2 or 3\n"))
        while not (inputNumber == "1" or inputNumber == "2" or inputNumber == "3"):
            inputNumber = int(input("Invalid input. Enter number of matches to delete: 1, 2 or 3\n"))
        numberOfMatches = numberOfMatches - inputNumber
        activePlayer = "c"
# while computer is playing he can cheat or not
    elif activePlayer == "c":
        if (numberOfMatches % 4) == 0 and (numberOfMatches >= 8 and numberOfMatches <= 20):
            toCheatOrNotToCheat = ["Cheat", "NotCheat"]
            cheatOrNot = random.choice(toCheatOrNotToCheat)
            if cheatOrNot == "Cheat":
                print("I delete 3")
                numberOfMatches = numberOfMatches - 4
            elif cheatOrNot == "NotCheat":
                randomDecision = random.randint(1, min(3, numberOfMatches))
                print("I delete ", randomDecision)
                numberOfMatches = numberOfMatches - randomDecision
        else:
            print("I delete ", (numberOfMatches % 4))
            numberOfMatches = numberOfMatches - (numberOfMatches % 4)
        activePlayer = "p"
    return activePlayer, numberOfMatches

# activating the function
while (numberOfMatches > 0):
    activePlayer, numberOfMatches = turn(activePlayer, numberOfMatches)

#result
if activePlayer == "p":
    print("I win and you lose")
else:
    print("You win")
#who wins