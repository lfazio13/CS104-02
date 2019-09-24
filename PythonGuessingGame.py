#Isabella Chiaravalloti, Yosef Davidowitz, Logan Fazio
import random
theComputerNumber = (random.randint(1,1000000))
gameOver = False
numberOfGuesses = 0
lowGuessRange = 1
highGuessRange = 1000000
guessesRemaining = 20

# This is the game loop
while gameOver != True:
    guess = int(input("Enter a guess in between: " + str(lowGuessRange) + " and " + str(highGuessRange) + ": "))
    numberOfGuesses += 1
    guessesRemaining -= 1
    while guess > highGuessRange or guess< lowGuessRange:
        guess = int(input("That number is not in the range. Enter a guess in between "  + str(lowGuessRange) + " and " + str(highGuessRange) + ": "))
    if guess < theComputerNumber:
        print("The number is greater than " + str(guess) + ".")
        lowGuessRange = guess
        print("You have " + str(guessesRemaining) + " guesses remaining.")
    elif guess > theComputerNumber:
        print("The number is lower than " + str(guess) + ".")
        highGuessRange = guess
        print("You have " + str(guessesRemaining) + " guesses remaining.")
    if guess == theComputerNumber:
        print("You guessed correct!")
        gameOver = True
    if numberOfGuesses == 20:
        print("You used too many guesses. The correct number was " + str(theComputerNumber) + ".")
        gameOver = True
    
    
