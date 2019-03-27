import os
from random_words import RandomWords

terminalSize = os.get_terminal_size().columns
# rules = ["Welcome to Hangman, Enter at your peril!",
#         "To play, one player must select a word to guess.",
#         "The other player must try to guess the word.",
#         "However, beware, you only have 6 lives!",
#         "If you reach 0 lives you DIE!",
#         "ENJOY!!!"]

rules = ["Welcome to Hangman, Enter at your peril!",
         "You man have up to two players.",
         "To play, one player must select a word to guess.",
         "The other player must try to guess the word.",
         "However, beware, you only have 6 lives!",
         "If you reach 0 lives you DIE!",
         "ENJOY!!!"]

for line in rules:
    print(line.center(terminalSize))

playAgain = True

while playAgain:
    players = input("How many players? ")
    if int(players) == 1:
        rw = RandomWords()
        word = rw.random_word()
    else:
        word = str(input("Please pick a word: ")).lower()
    os.system('clear')
    playerGuess = None
    lettersGuessed = []
    guessedWord = []
    for i in word:
        guessedWord.append("_ ")
    guesses = None
    print("You have 6 lives! GO!!")
    remainingLives = 5

    while (remainingLives != 0 and "_ " in guessedWord):
        print(f"You have {remainingLives} lives remaining!")
        guesses = "".join(guessedWord)
        print(guesses)
        # This is for error validation.
        try:
            playerGuess = str(input("Please select a letter: ")).lower()
        except:
            print("That is not a valid input. Please try again...")
            continue
        else:
            if not playerGuess.isalpha():
                print("That is not a valid input. Please try again...")
                continue
            elif len(playerGuess) > 1:
                print("You have already guessed that letter. Please try again...")
            else:
                pass

            lettersGuessed.append(playerGuess)

        for i in range(len(word)):
            if playerGuess == word[i]:
                guessedWord[i] = playerGuess

        if playerGuess not in word:
            remainingLives -= 1
            print(f"You have {remainingLives} lives remaining! Careful!")
    if "_ " not in guessedWord:
        print(f"Congratulations, You guessed the word: {word}!!!!")
    else:
        print(f"Whelp! You are pretty unlucky, the word was: {word}!")

    print("Do ya' want to play again?")
    response = input(">> ").lower()
    if response not in ("yes", "y"):
        playAgain = False
