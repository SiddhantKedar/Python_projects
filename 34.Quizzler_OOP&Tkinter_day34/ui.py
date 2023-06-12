from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=30, pady=30)

        self.score = Label(text="Score 0", background=THEME_COLOR, foreground="white")
        self.score.grid(column=2, row=1)

        self.question_display = Canvas(width=300, height=250)
        self.question_display.grid(column=1, row=2, columnspan=2, pady=20)
        self.question = self.question_display.create_text(150, 125,
                                                          width=280,
                                                          text="Question goes here",
                                                          font=("Arial", 20, "italic"), fill=THEME_COLOR)

        right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_img, background=THEME_COLOR, highlightthickness=0, command=self.right_pressed)
        self.right_button.grid(column=1, row=3)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img, background=THEME_COLOR, highlightthickness=0, command=self.wrong_pressed)
        self.wrong_button.grid(column=2, row=3)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.question_display.config(background="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_display.itemconfig(self.question,text=q_text)
        else:
            self.question_display.itemconfig(self.question, text="You have readvhed the end")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_display.config(background="green")
        else:
            self.question_display.config(background="red")
        self.window.after(1000, func= self.get_next_question)
