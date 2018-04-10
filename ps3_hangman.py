# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
secretWordList = list(secretWord)
newWord =len(secretWordList)*['_ ']


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    for i in range (len(secretWordList)):

        if secretWordList[i] in set(lettersGuessed):
            newWord[i]= secretWordList[i]
    result = ''.join(newWord)
    return result

aletters = string.ascii_lowercase
aletterslist = list(string.ascii_lowercase)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in aletterslist:
            aletterslist.remove(lettersGuessed[i])
    result = ''.join(aletterslist)
    return result
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    mistakesMade = 8
    wordGuessed = False
        
    print('Welcome to the game, Hangman!')
    print(('I am thinking of a word that is ') + intro + (' letters long.'))
    print ('------------')

    while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print(('You have ') + str(mistakesMade) + (' guesses left.'))
        print(('Available letters: ') + str(getAvailableLetters(lettersGuessed)))
        guess = input('Please guess a letter: ').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print(("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed))
                print('------------')
            else:
                lettersGuessed.append(guess)
                print(('Good guess: ') + getGuessedWord(secretWord, lettersGuessed))
                print('------------')
        else:
            if guess in lettersGuessed:
                print(("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print(('Oops! That letter is not in my word: ') + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')

    if wordGuessed == True:
        print('Congratulations, you won!')
    elif mistakesMade == 0:
        print(('Sorry, you ran out of guesses. The word was ') + secretWord)   



hangman(secretWord)