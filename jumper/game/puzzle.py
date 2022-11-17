import random

# Class declaration.
class Puzzle:
    """The part holding the secret word, and giving hints. 
    
    The responsibility of a Puzzle is to keep track of the secret word
    
    Attributes:
        _secretWord: The secret word that is being guessed
        _displayString: The representation to the user of which letters have been guessed correctly
    """

    # Create the class constructor.
    def __init__(self):
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        words = ["cat", "dog", "class", "mississippi"]
        self._secretWord = words[random.randint(0, len(words) - 1)]

        self._displayString = ""
        self._displayStringArray = []

        for ch in self._secretWord:
            self._displayStringArray.append("_ ")
            self._displayString += "_ "
       
    def get_displayString(self):
        """Gets the current _displayString.
        
        Returns:
            _displayString: Shows which letters the user has guessed correctly
        """
        return self._displayString

    def checkGuess(self, letter): 
        """Checks the guessed letter from the user and updates the guessed string
    
        Parameter(s)
            letter: the guessed letter
        Return: guessed: a boolean if the guessed letter was found in the secrt word
        """
        guessed = False
        self._displayString = ""
        for _ in range(len(self._secretWord)):
            if letter == self._secretWord[_]:
                self._displayStringArray[_] = self._secretWord[_] + " "
                guessed = True
            self._displayString += self._displayStringArray[_]
        return guessed

    def is_complete(self): 
        """Checks to see if the puzzle is solved
    
        Parameter(s)
            self: 
        Return: self: and instance of [uzzle]
        """
        complete = True
        checkString = []

        for ch in self._displayStringArray:
            checkString.append(ch)

        for i in range(len(self._secretWord)):
            if not checkString[i][0] == self._secretWord[i]:
                complete = False
    
        return complete
