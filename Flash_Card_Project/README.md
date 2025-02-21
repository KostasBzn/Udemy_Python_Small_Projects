# Flashcard App

A simple flashcard application built with Python and Tkinter to help you learn French words. The app displays a French word and its English translation after a few seconds. You can mark words as "learned," and they will be excluded from future sessions.

## Features

- **Dynamic Word Selection**: Randomly selects words from a CSV file (`french_words.csv`).
- **Learned Words Tracking**: Tracks learned words in a separate CSV file (`data_learned.csv`).
- **Automatic Flip**: Automatically flips the card to show the English translation after 3 seconds.
- **Responsive UI**: Clean and intuitive user interface with buttons to mark words as learned or to skip.

## How It Works

1. **Word Selection**:

   - The app reads a list of French words and their English translations from `french_words.csv`.
   - It excludes words that are already marked as learned in `data_learned.csv`.

2. **Card Display**:

   - Displays a French word on the front of the card.
   - After 3 seconds, the card flips to show the English translation.

3. **Marking Words as Learned**:

   - Click the green checkmark button (✅) to mark the current word as learned.
   - The word is added to `data_learned.csv` and excluded from future sessions.

4. **Skipping Words**:
   - Click the red cross button (❌) to skip the current word and show a new one.

## Requirements

- Python 3.x
- Pandas (`pip install pandas`)
- Tkinter (pre-installed with Python)

## 🚀 How to Run the FlashCard

1. Clone the repository or download the files.
2. Navigate to the folder containing the game files.
3. Install the required libraries `pip install -r requirements.txt`
4. Run the `main.py` script: `python main.py`
