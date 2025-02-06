from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for q in question_data[0]["results"]:
    question = Question(q["question"], q["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
