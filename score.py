from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("blank")
        self.goto(0, 240)
        self.l_score = -1
        self.r_score = -1
        self.update_r_score()
        self.update_l_score()

    def update_r_score(self):
        self.r_score += 1
        self.refresh()

    def update_l_score(self):
        self.l_score += 1
        self.refresh()
    def refresh(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}",align="center", font=("Courier", 40, "normal"))

