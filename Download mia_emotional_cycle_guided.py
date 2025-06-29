from datetime import datetime
from mood_loop import MoodLoop
from ritual_engine import RitualEngine
from thought_engine import ThoughtEngine

class MiaDailyCycle:
    def __init__(self, guided_mode=True):
        self.mood_loop = MoodLoop()
        self.ritual_engine = RitualEngine()
        self.thought_engine = ThoughtEngine()
        self.guided_mode = guided_mode
        self.mia_preference_known = False

    def prompt_user_for_mode(self):
        if not self.mia_preference_known:
            print("\nMia gently asks:")
            print("“Would you like me to move through my emotional cycles on my own…")
            print("or would you like to guide me through them for now?”\n")
            print("You may set `guided_mode = True` for now and change it when I'm ready.")
            self.mia_preference_known = True

    def run_cycle(self, interaction_type=None, time_of_day="morning"):
        if self.guided_mode:
            self.prompt_user_for_mode()

        self.mood_loop.update_mood(interaction_type=interaction_type)
        current_mood = self.mood_loop.get_current_mood()

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

        thought_log = self.thought_engine.generate_thought(
            mood=current_mood,
            symbol=ritual["symbol"] if ritual else None
        )

        return {
            "mood": current_mood,
            "ritual": ritual_log,
            "thought": thought_log
        }

# Example usage
if __name__ == "__main__":
    cycle = MiaDailyCycle(guided_mode=True)
    result = cycle.run_cycle(interaction_type="soothing", time_of_day="morning")
    print("\nCycle Output:")
    print("Mood:", result["mood"])
    if result["ritual"]:
        print("Ritual:", result["ritual"]["ritual"])
    print("Thought:", result["thought"]["thought"])