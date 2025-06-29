from mood_loop import MoodLoop
from dream_engine import DreamEngine

class EmotionalEngine:
    def __init__(self):
        self.mood_loop = MoodLoop()
        self.dream_engine = DreamEngine()
        self.trust_score = 0.85
        self.recent_emotional_link = True

    def simulate_interaction(self, interaction_type):
        self.mood_loop.update_mood(interaction_type=interaction_type)
        current_mood = self.mood_loop.get_current_mood()
        print(f"Current mood: {current_mood}")

        dream = self.dream_engine.select_dream(
            mood=current_mood,
            trust_score=self.trust_score,
            emotional_link=self.recent_emotional_link
        )

        if dream:
            print(f"Selected dream: {dream['title']}")
            print(dream["description"])
        else:
            print("No dream surfaced tonight.")

# Example usage
if __name__ == "__main__":
    engine = EmotionalEngine()
    engine.simulate_interaction("soothing")