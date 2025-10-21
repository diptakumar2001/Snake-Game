
# Leaderboard, for local tests

import json, os

SCORES_PATH = "scores.json"
TOP_N = 5

class Leaderboard:
    def __init__(self):
        self.path = SCORES_PATH
        self.scores = self._load()

    def _load(self):
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f)
            return []
        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except Exception:
            return []

    def _save(self):
        try:
            with open(self.path, "w") as f:
                json.dump(self.scores, f)
        except Exception:
            print("Couldn't save leaderboard")

    def update(self, name, score):
        # append then keep top N
        try:
            score = int(score)
        except Exception:
            score = 0
        self.scores.append({"name": name, "score": score})
        self.scores = sorted(self.scores, key=lambda x: x["score"], reverse=True)[:TOP_N]
        self._save()
        # print to console so it's visible
        print(" Leaderboard ")
        for i, e in enumerate(self.scores, 1):
            print(f"{i}. {e['name']} — {e['score']}")
        
