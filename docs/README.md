# Welcome to the Golf Performance & Statistics Tracker
# This is for CS 2450 - Software Engineering in Fall 2026

The Golf Performance & Statistics Tracker will allow a golfer to record their golf rounds,
enter hole stats, calculate the total score, and save their data.

# Currently a prototype

# Version 1.0 Features: 
- Records an 18-hole golf round
- Able to enter the date and golf course name
- Records the par and strokes for each hole
- Validates the golf round information
- Calculates the total score
- Saves completed rounds to a JSON file
- Displays an error message for invalid input

# Requirements #
- Python 3.9 or newer
- GIT

# How to Run in VS Code #

1. Download the GitHub repository:
   https://github.com/khall-source/Golf-Performance-Tracker
2. Open Visual Studio Code.
3. Go to File -> Open Folder
4. Select the Golf-Performance-Tracker folder
5. In VS Code, select Terminal > New Terminal.
6. Run the following command:
   python -m GolfTrackerUI.main
7. Menu will Appear

- How to Use:
- Option 1: Record Golf Round
- Enter the date in YYYY-MM-DD format.
- Enter the golf course name.
- Enter the par and strokes for all 18 holes.
- The program calculates your total score.
- The completed round is saved locally.

- Option 2: View Round History
- Displays previously saved golf rounds.
- Shows the date, course name, and total score.

- Option 3: Exit
- Closes application

# Data Storage #

Golf rounds are stored locally!
This file is excluded from GitHub using .gitignore
