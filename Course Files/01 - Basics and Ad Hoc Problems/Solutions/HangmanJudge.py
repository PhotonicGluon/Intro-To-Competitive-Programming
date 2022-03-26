# Read in the data
while True:
    # Get the round number
    roundNum = int(input())
    
    # If round number is "-1" terminate
    if roundNum == -1:
        break
        
    # Get the actual word and the guessed letters
    actualWord = input()
    guesses = input()
    
    # Simulate the game
    strikes = 0
    seenGuesses = set()
    
    for char in guesses:
        # Check if already guessed
        if char not in seenGuesses:
            # Count the number of occurances
            if actualWord.find(char) == -1:  # None found
                strikes += 1
            else:
                actualWord = actualWord.replace(char, "")  # Remove the character

            # Add the current guess to the set of seen guesses
            seenGuesses.add(char)
            
        # Check ending conditions
        if strikes == 7:
            break
        elif actualWord == "":
            break
    
    print(f"Round {roundNum}")
    if strikes == 7:
        print("You lose.")
    elif actualWord == "":
        print("You win.")
    else:
        print("You chickened out.")