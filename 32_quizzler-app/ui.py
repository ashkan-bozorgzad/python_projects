from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lable = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_lable.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0, )
        self.text = self.canvas.create_text(150,
                                            125,
                                            width=280,
                                            text="text",
                                            fill=THEME_COLOR,
                                            font=("Aerial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        self.known_button = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0, command=self.true_button)
        self.known_button.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.unknown_button = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, command=self.false_button)
        self.unknown_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.score_lable.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")
            self.known_button.config(state="disabled")
            self.unknown_button.config(state="disabled")

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)
