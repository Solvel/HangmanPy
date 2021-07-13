import random as ran        # Random number generator to chose a word
import requests             # For the dictionary import

# Import the English dictionary
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
words = response.content.splitlines()

# Get a random number within the size of the dictionary
ranNum = ran.randint(0, len(words)-1)

# Pick the word based on the random number, and remove the b-prefix
chosenWord = words[ranNum].decode('utf-8')

# Declaration of variables
dashes = ""
foundLetters = ""
guesses = ""
lives = 6

# Print out dashes to visualize the length of the word
for i in range(len(chosenWord)):
    dashes += '-'

# Printing out the UI
print("\nHangman!" + "\n")
print(dashes)
#print(chosenWord)

# Function to check if the chosen word contains the guessed letter
def checkLetters():
    win = 0                                         # Resets the win condition before the loop
    print(chr(27) + "[2J")                          # Clears the terminal
    print("Guesses: " + guesses + "\n")             # Shows previous guesses
    for i in range(len(chosenWord)):
        if(foundLetters.find(chosenWord[i]) != -1): # If the guess is correct
            print(chosenWord[i],  end = '')         # Print the current state of the word  
            win += 1                    
        else:
            if(lives != 0):
                print('-', end='')                  # Print missing characters as "-"
        if(win == len(chosenWord)):                 # Win condition (size of word)
            print("\nYou win!")
            exit()

while(lives != 0):                                  # Game loop
    guess = input("\n\nGuess a letter!")            # Take the guess input
    guesses += guess                                # Collect previous guesses
    if(chosenWord.find(guess) != -1):               # If the word contains guessed character
        foundLetters += guess                       # Add it to found characters
        checkLetters()                              # Runs the character checker
    else:
        if(guesses.count(guess) == 1):              # If the guess is wrong
            lives -= 1                              # Remove a life
        checkLetters()
        if(lives != 0):                             
            print("\n\nWrong, try again! Lives: " + str(lives))

if(lives == 0):                                     # Lose condition
    print(chr(27) + "[2J")       
    print("You lost!")

