class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = q_bank

    def still_has_questions(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            print("You have completed the challenge!")
            print(f"Your final score is {self.score}/{self.question_number}")
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q_{self.question_number}. {current_question.text} (True or False): ")
        self.check_answer(user_input, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

