from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.chute import Chute


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        puzzle (Puzzle): The game's puzzle.
        is_playing (boolean): Whether or not to keep playing.
        chute (Chute): The game's chute.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._is_playing = True
        self._chute = Chute()
        self._terminal_service = TerminalService()
        self._guess = ""
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._do_outputs()
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        self._terminal_service.write_text("Thanks for playing!")

    def _get_inputs(self):
        """Gets a guess from the user

        Args:
            self (Director): An instance of Director.
        """
        self._guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        
    def _do_updates(self):
        """Checks if the guess is in the secret word

        Args:
            self (Director): An instance of Director.
        """
        if not self._puzzle.checkGuess(self._guess):
            self._chute.cutChute()
        self._is_playing = not self._puzzle.is_complete()
        
    def _do_outputs(self):
        """Prints if the guessed letter was in the secret word and the parachute man

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text(f"\n{self._puzzle.get_displayString()}\n")
        self._terminal_service.write_list(self._chute.get_chute())
        if self._chute.is_chuteGone():
            self._is_playing = False
            self._terminal_service.write_text("GAME OVER")