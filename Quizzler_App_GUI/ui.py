from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.score_num = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.v_image = PhotoImage(file='./images/true.png')
        self.x_image = PhotoImage(file='./images/false.png')
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)

        self.v_button = Button(image=self.v_image, command=self.correct, highlightthickness=0)
        self.x_button = Button(image=self.x_image, command=self.false, highlightthickness=0)
        self.score = Label(text=f"Score: {0}", font=("Arial", 10, "italic"), bg=THEME_COLOR, fg="white")
        self.question_label = self.canvas.create_text(150, 125, text="Hi question!", font=("Arial", 15, "italic"), fill=THEME_COLOR, width=280)

        self.score.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.v_button.grid(column=0, row=2)
        self.x_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=q_text)
        else:
            self.canvas.itemconfig(self.question_label, text="You have reached the end of the Quizzer!")
            self.v_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def correct(self):
        is_correct = self.quiz.check_answer("true")
        self.answer_feedback(is_correct)
    def false(self):
        is_correct = self.quiz.check_answer("false")
        self.answer_feedback(is_correct)
        
        
        

    def answer_feedback(self, feedback):
        if feedback:
            self.canvas.config(bg='green')
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, lambda: self.canvas.config(bg='white'))
        self.window.after(1000, lambda: self.get_next_question()) 

