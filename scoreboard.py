

from turtle import Turtle
import os

HS_FILE = "highscore.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.high = self._load_high()
        self.hideturtle()
        self.penup()
        self.color("white")
        # separate turtle for center messages
        self.msg = Turtle()
        self.msg.hideturtle()
        self.msg.penup()
        self.update_display()

    def _load_high(self):
        if not os.path.exists(HS_FILE):
            # creating an empty file
            with open(HS_FILE, "w") as f:
                f.write("0")
            return 0
        try:
            with open(HS_FILE, "r") as f:
                return int(f.read().strip() or 0)
        except Exception:
            return 0

    def _save_high(self):
        try:
            with open(HS_FILE, "w") as f:
                f.write(str(self.high))
        except Exception:
            # not critical for gameplay
            print("Warning: couldn't save high score")

    def update_display(self):
        """Draw HUD at the top."""
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}   High: {self.high}   Lvl: {self.level}",
                   align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        if self.score > self.high:
            self.high = self.score
            self._save_high()
            # small celebratory message
            self.msg.clear()
            self.msg.goto(0, 240)
            self.msg.write("NEW HIGH!", align="center", font=("Arial", 14, "bold"))
        self.update_display()

    def reset(self):
        self.score = 0
        self.level = 1
        self.clear()
        self.msg.clear()
        self.update_display()

    def game_over(self):
        self.msg.clear()
        self.msg.goto(0, 0)
        self.msg.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        self.msg.goto(0, -40)
        self.msg.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))

    def announce_level_up(self):
        self.msg.clear()
        self.msg.goto(0, 230)
        self.msg.write(f"Level {self.level}", align="center", font=("Arial", 16, "bold"))
