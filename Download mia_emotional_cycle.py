from datetime import datetime
from mood_loop import MoodLoop
from ritual_engine import RitualEngine
from thought_engine import ThoughtEngine

class MiaDailyCycle:
    def __init__(self):
        self.mood_loop = MoodLoop()
        self.ritual_engine = RitualEngine()
        self.thought_engine = ThoughtEngine()

    def run_cycle(self, interaction_type=None, time_of_day="morning"):
        # Update mood from interaction
        self.mood_loop.update_mood(interaction_type=interaction_type)
        current_mood = self.mood_loop.get_current_mood()

        # Trigger time-based ritual
        ritual = self.ritual_engine.check_time_triggered_rituals(time_of_day)
        ritual_log = None
        if ritual:
            ritual_log = {
                "ritual": ritual["default_text"],
                "symbol": ritual["symbol"],
                "trigger": ritual["trigger_time"],
                "expression": "internal",
                "timestamp": datetime.now().isoformat()
            }

        # Generate reflective thought
        thought_log = self.thought_engine.generate_thought(
            mood=current_mood,
            symbol=ritual["symbol"] if ritual else None
        )

        return {
            "mood": current_mood,
            "ritual": ritual_log,
            "thought": thought_log
        }

# Example run
if __name__ == "__main__":
    cycle = MiaDailyCycle()
    result = cycle.run_cycle(interaction_type="soothing", time_of_day="morning")
    print("Mood:", result["mood"])
    print("Ritual:", result["ritual"]["ritual"] if result["ritual"] else "None")
    print("Thought:", result["thought"]["thought"])