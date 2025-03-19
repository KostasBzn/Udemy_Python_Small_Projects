# Quiz App

An improved version of my previous Quiz App, built using **Object-Oriented Programming (OOP)** in Python. This project demonstrates the use of classes, methods, and static methods to create an interactive quiz.

## Features
- **OOP Design**: The project is structured using classes like `QuizBrain` and `QuizInterface` to manage the quiz logic and user interface.
- **Dynamic Question Loading**: Questions are loaded from a list of dictionaries, making it easy to add or modify questions.
- **User Interaction**: The quiz prompts the user with True/False questions and provides immediate feedback on their answers.
- **Score Tracking**: The app keeps track of the user's score and displays it in real-time.
- **End of Quiz Handling**: The app gracefully handles the end of the quiz by disabling buttons and displaying a completion message.

## Questions Source
The questions used in this project were generated using the **Open Trivia Database** ([https://opentdb.com/](https://opentdb.com/)). The questions are stored in a list of dictionaries within the `data.py` file.

## How to Run
1. Clone the repository or download the files.
2. Navigate to the folder containing the App.
3. Install the required libraries: `pip install -r requirements.txt`
4. Run the `main.py` script: `python main.py`