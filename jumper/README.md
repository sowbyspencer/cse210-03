# Jumper
Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

---
## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 seeker 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                      (project root folder)
+-- jumper                (source code for game)
  +-- game                (specific classes)
    +-- director.py       (processes the logic of the game)
    +-- chute.py          (holds info about the man and parachute, and methods to change itself)
    +-- puzzle.py         (holds info about the secret word, the hint display and methods to change itself and check guesses)
    +-- terminal_service  (all user input and output goes through this class)
  +-- __main__.py         (program entry point)
+-- README.md             (general info)
```

### director.py
| class: director |
| --- |
| __init__(self) |
| _puzzle: Puzzle |
| _is_playing: True |
| _chute: Chute |
| _terminal_service: TerminalService |
| _guess: string |
|  |
| start_game(self) |
| _get_inputs(self) |
| _do_updates(self) |
| _do_outputs(self) |

### puzzle.py
| class: puzzle |
| --- |
| __init__(self) |
| words: lsit |
| _secretWord: string |
| _displayStringArray: list |
| _displayString: string |
|  |
| get_displayString(self): string |
| checkGuess(self, letter): boolean |
| is_complete(self) : boolean |


## Required Technologies
* Python 3.8.0

## Authors
* Spencer Sowby (sow22003@byui.edu)
