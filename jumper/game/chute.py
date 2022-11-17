import random

class Chute:
    """
    
    
    
    Attributes:
        _chuteList (list): The list that represents the man and his parachute
    """

    def __init__(self):
        """Constructs a new Chute.

        Args:
            self (Chute): An instance of Chute.
        """
        self._chuteList = ["  ___  ", " /___\ ", " \   / ", "  \ /  ", "   0   ", "  /|\  ", "  / \  ", "       ", "^^^^^^^"]

    def get_chute(self): 
        """ Returns an array of the representation of the man and parachute
        """
        return self._chuteList
        
    def is_chuteGone(self): 
        """Returns if the chute is gone
    
        Parameter(s)
            self: 
        Return: a boolean True if the chute is gone
        """
        if len(self._chuteList) <= 5:
            self._chuteList[0] = "   x   "
        return len(self._chuteList) <= 5

    def cutChute(self): 
        """Cuts the top line of the parachuet
    
        Parameter(s)
            self: 
        Return: chuteList: A list that is a representation of the man and parachute
        """
        self._chuteList.pop(0)
        