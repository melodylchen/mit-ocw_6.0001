# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
#FYI, need to change terminal to working directory of ps2

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    word_letters = list(secret_word)
    answer = True
    for letter in secret_word:
      if letter not in letters_guessed:
        answer = False
    return answer
"""
#Testing for is_word_guessed
secret_word = 'apple'
letters_guessed = ['a', 'i', 'k', 'p', 'r', 's']
print(is_word_guessed(secret_word, letters_guessed))
#Output should be False

secret_word = 'apple'
letters_guessed = ['f', 'a', 'p', 'l', 'e', 'z']
print(is_word_guessed(secret_word, letters_guessed))
#Output should be True
"""

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_letters = list(secret_word)
    answer = list('_'*len(secret_word))
    for letter in letters_guessed:
      if letter in word_letters:
        for i in range(len(word_letters)):
          if word_letters[i] == letter:
            answer[i]=word_letters[i]
    return " ".join(answer)
"""
test for above function   
secret_word = 'apple'
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
print(get_guessed_word(secret_word, letters_guessed))
#Answer should be '_ p p _ e'
"""

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = list(string.ascii_lowercase)
    for letter in letters_guessed:
      if letter in available_letters:
        for i in range(len(available_letters)):
          if available_letters[i] == letter:
            available_letters[i]= ""
    return "".join(available_letters)


#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']  
#print(get_available_letters(letters_guessed))

# should be: abcdfghjlmnoqtuvwxyz


    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #Add constants
    num_guesses = 6
    num_warnings = 3
    letters_guessed = []   
    vowels = ['a','e','i','o','u']
    space = "---------------------"
    print("Welcome to the game Hangman!\nI was thinking of a word that is",len(secret_word),"letters long.")
    print("_ "*len(secret_word))
    print("You have", num_warnings, "warnings left.")
    print(space)
    print("You have", num_guesses, "guesses left.")
    print("Available letters:", get_available_letters(letters_guessed))


    while num_guesses >= 0:
      if num_guesses == 0:
        print("Sorry, you ran out of guesses. The word was", secret_word)
        break
      elif is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your total score for this game is:", num_guesses*len(set(secret_word)))
        print(get_guessed_word(secret_word, letters_guessed))
        break
      userguess = str.lower(input("Please guess a letter:"))
      if userguess.isalpha() is False:
        if num_guesses == 0:
          print("Sorry you have lost!")
          break
        elif num_warnings == 0 and num_guesses > 0:
          num_guesses = num_guesses - 1
          print('3 warnings have been used. Number of guesses left:', num_guesses)
          print(get_guessed_word(secret_word, letters_guessed))
          print(space)
          print("Available letters left:", get_available_letters(letters_guessed))
        elif num_warnings > 0:
          num_warnings = num_warnings - 1
          print("Oops! That is not a valid letter. You have", num_warnings, "warnings left:", get_guessed_word(secret_word, letters_guessed))
          print(space)
          print("Available letters left:", get_available_letters(letters_guessed))

      else:
        if userguess in letters_guessed:
          if num_warnings > 0:
            num_warnings = num_warnings - 1
            print("Oops! You've already guessed that letter. You now have", num_warnings, "warnings:", get_guessed_word(secret_word, letters_guessed))
            print(space)
            print("Available letters left:", get_available_letters(letters_guessed))
          else:
            if num_guesses < 1:
              print("Sorry you lost!")
              print("The word was", secret_word)
              break
            else:
              num_guesses = num_guesses - 1
              print(space)
              print("You have", num_guesses, 'guesses left')
              print("Available letters left:", get_available_letters(letters_guessed))
        elif userguess not in list(secret_word):
          letters_guessed.append(userguess)
          if userguess in vowels:
            num_guesses = num_guesses - 2
          else:
            num_guesses = num_guesses - 1
          print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
          print(space)
          print("You have", num_guesses, "guesses left.")
          print("Available letters left:", get_available_letters(letters_guessed))
        else:
          letters_guessed.append(userguess)
          print("Good guess:", get_guessed_word(secret_word, letters_guessed))
          print(space)
          print("Number of guesses left:", num_guesses)
          print("Available letters left:", get_available_letters(letters_guessed))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
