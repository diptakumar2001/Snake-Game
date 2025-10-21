import json
import os

LEADERBOARD_FILE = "scores.json"
TOP_SCORES = 5

class Leaderboard:
    def __init__(self):
        self.file_path = LEADERBOARD_FILE
        self.scores = self.load_scores()

    def load_scores(self):
        # Load scores from file
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump([], file)
            return []
        
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except:
            return []

    def save_scores(self):
        # Save scores to file
        try:
            with open(self.file_path, "w") as file:
                json.dump(self.scores, file, indent=2)
        except:
            print("Couldn't save leaderboard")

    def update(self, player_name, score):
        # Add a new score and keep only top scores
        try:
            score = int(score)
        except:
            score = 0
        
        # Add new score
        self.scores.append({"name": player_name, "score": score})
        
        # Sort by score and keep only top scores
        self.scores.sort(key=lambda x: x["score"], reverse=True)
        self.scores = self.scores[:TOP_SCORES]
        
        self.save_scores()
        self.display()

    def display(self):
        # Print leaderboard to console
        print("\n" + "="*30)
        print("LEADERBOARD")
        print("="*30)
        for i, entry in enumerate(self.scores, 1):
            print(f"{i}. {entry['name']} - {entry['score']} points")
        print("="*30 + "\n")