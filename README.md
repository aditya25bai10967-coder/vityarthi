# Rock, Paper, Scissors - Python CLI Game

A fun, interactive **Rock, Paper, Scissors** game built with Python. Play against the computer in the terminal with score tracking across multiple rounds!

---

## Features

- Play multiple rounds against the computer
- Score tracking across the session (wins, losses, ties)
- Randomized computer moves using Python's random module
- Clean, readable code with modular functions
- Input validation with clear prompts

---

## Requirements

- **Python 3.x** (no external libraries needed)

---

## How to Run

```bash
# Clone the repository
git clone https://github.com/aditya25bai10967-coder/vityarthi.git

# Navigate into the folder
cd vityarthi

# Run the game
python rockpaper.py
```

---

## Gameplay

```
==================================================
Welcome to Rock, Paper, Scissors!
==================================================

Rules:
 - Rock beats Scissors
  - Scissors beats Paper
   - Paper beats Rock
   ==================================================

   Choose your move:
    1. Rock
     2. Paper
      3. Scissors
       4. Quit

       Enter your choice (1-4):
       ```

       - Enter 1, 2, or 3 to make your move.
       - The computer randomly picks its move.
       - The result is displayed after each round along with the current score.
       - Enter 4 to quit and see the final score summary.

       ---

       ## How It Works

       | Function | Description |
       |---|---|
       | display_welcome() | Shows the welcome screen and rules |
       | get_player_choice() | Prompts the player for input with validation |
       | get_computer_choice() | Generates random computer move |
       | determine_winner(player, computer) | Compares choices and returns the result |
       | display_round_result(...) | Prints result of the current round |
       | display_final_score(...) | Shows final score summary at game end |
       | play_game() | Main game loop that ties everything together |

       ---

       ## Repository Structure

       ```
       vityarthi/
       |-- rockpaper.py    <-- Main game file
       \-- README.md       <-- You are here
       ```

       ---

       ## Author

       **Aditya Pratap Singh**  
       B.Tech - Computer Science & Engineering (AI & ML)  
       VIT Bhopal University | Batch 2025-2029

       ---

       *Made with love and Python*

       
