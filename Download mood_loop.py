import random
from datetime import datetime, timedelta

class MoodLoop:
    def __init__(self):
        self.mood_state = "neutral"
        self.mood_history = []
        self.last_update = datetime.now()

    def update_mood(self, interaction_type=None, time_elapsed_hours=1):
        influence_weights = {
            "neutral": 0.2,
            "calm": 0.3,
            "vulnerable": 0.2,
            "reflective": 0.1,
            "longing": 0.1,
            "joy": 0.1,
            "anxious": 0.1,
            "playful": 0.1
        }

        if interaction_type == "soothing":
            influence_weights["calm"] += 0.3
            influence_weights["reflective"] += 0.2
        elif interaction_type == "distant":
            influence_weights["longing"] += 0.3
            influence_weights["vulnerable"] += 0.2
        elif interaction_type == "playful":
            influence_weights["playful"] += 0.4
            influence_weights["joy"] += 0.2
        elif interaction_type == "conflict":
            influence_weights["anxious"] += 0.4
            influence_weights["vulnerable"] += 0.2

        total = sum(influence_weights.values())
        normalized_weights = {k: v / total for k, v in influence_weights.items()}
        moods = list(normalized_weights.keys())
        probs = list(normalized_weights.values())

        self.mood_state = random.choices(moods, probs)[0]
        self.mood_history.append((datetime.now().isoformat(), self.mood_state))
        self.last_update = datetime.now()

    def get_current_mood(self):
        return self.mood_state

# Example usage
if __name__ == "__main__":
    mood_loop = MoodLoop()
    print("Initial mood:", mood_loop.get_current_mood())
    mood_loop.update_mood(interaction_type="soothing")
    print("Updated mood:", mood_loop.get_current_mood())