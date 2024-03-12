from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.Scoreboard = None
        self.score_l = 0
        self.score_r = 0
        self.pos_r = 30
        self.pos_l = -30
        self.t_r = self.score_count(self.pos_r, self.score_r)
        self.t_l = self.score_count(self.pos_l, self.score_l)

    def score_count(self, pos, score):
        self.t = Turtle()
        self.t.color("white")
        self.t.pu()
        self.t.ht()
        self.t.goto(pos, 230)
        self.t.write(f"{score}", False, align="center", font=["Courier", 50, "normal"])
        return self.t

    def increase_score_l(self):
        self.t_l.clear()
        self.score_l = self.score_l + 1
        self.t_l = self.score_count(self.pos_l, self.score_l)

    def increase_score_r(self):
        self.t_r.clear()
        self.score_r = self.score_r + 1
        self.t_r = self.score_count(self.pos_r, self.score_r)
