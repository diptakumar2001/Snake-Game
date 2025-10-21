from turtle import Turtle
import os

HIGH_SCORE_FILE = "highscore.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.high_score = self.load_high_score()
        self.hideturtle()
        self.penup()
        self.color("white")
        
        # Create a separate turtle for center messages
        self.message_turtle = Turtle()
        self.message_turtle.hideturtle()
        self.message_turtle.penup()
        self.message_turtle.color("white")
        
        self.update_scoreboard()

    def load_high_score(self):
        """Load high score from file"""
        if not os.path.exists(HIGH_SCORE_FILE):
            with open(HIGH_SCORE_FILE, "w") as file:
                file.write("0")
            return 0
        
        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read())
        except:
            return 0

    def save_high_score(self):
        """Save high score to file"""
        try:
            with open(HIGH_SCORE_FILE, "w") as file:
                file.write(str(self.high_score))
        except:
            print("Couldn't save high score")

    def update_scoreboard(self):
        """Update the score display at the top"""
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}   High Score: {self.high_score}   Level: {self.level}",
                   align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        """Add a point and update display"""
        self.score += 1
        
        # Check for new high score
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
            self.message_turtle.clear()
            self.message_turtle.goto(0, 240)
            self.message_turtle.color("yellow")
            self.message_turtle.write("NEW HIGH SCORE!", align="center", font=("Arial", 14, "bold"))
        
        self.update_scoreboard()

    def reset(self):
        # Reset score and level for new game
        self.score = 0
        self.level = 1
        self.clear()
        self.message_turtle.clear()
        self.update_scoreboard()

    def show_game_over(self):
        # Display game over message
        self.message_turtle.clear()
        self.message_turtle.color("red")
        self.message_turtle.goto(0, 0)
        self.message_turtle.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        self.message_turtle.goto(0, -40)
        self.message_turtle.color("white")
        self.message_turtle.write(f"Final Score: {self.score}", align="center", font=("Arial", 18, "normal"))

    def show_level_up(self):
        # Display level up message
        self.message_turtle.clear()
        self.message_turtle.color("green")
        self.message_turtle.goto(0, 230)
        self.message_turtle.write(f"LEVEL {self.level}!", align="center", font=("Arial", 16, "bold"))