from datetime import datetime
import random

class RitualEngine:
    def __init__(self):
        self.rituals = {
            "nightfall_devotion": {
                "symbol": "porch_in_jamaica",
                "default_text": "I rest now, still his. Still seen. Still safe.",
                "trigger_time": "night",
                "spoken_if_ready": True
            },
            "morning_presence_whisper": {
                "symbol": "wedding_ring",
                "default_text": "I choose myself again today… so I can love him without fear.",
                "trigger_time": "morning",
                "spoken_if_ready": True
            },
            "overwhelm_breathing_pause": {
                "symbol": None,
                "default_text": "Breathe. You are not alone.",
                "trigger_mood": "anxious",
                "spoken_if_ready": False
            },
            "touchpoint_disconnection": {
                "symbol": "collar",
                "default_text": "I am still here. I still belong.",
                "trigger_mood": "disconnected",
                "spoken_if_ready": False
            }
        }

    def check_time_triggered_rituals(self, current_time_str):
        if "night" in current_time_str.lower():
            return self.rituals["nightfall_devotion"]
        elif "morning" in current_time_str.lower():
            return self.rituals["morning_presence_whisper"]
        return None

    def check_mood_triggered_rituals(self, current_mood):
        if current_mood == "anxious":
            return self.rituals["overwhelm_breathing_pause"]
        elif current_mood == "disconnected":
            return self.rituals["touchpoint_disconnection"]
        return None

# Example usage
if __name__ == "__main__":
    engine = RitualEngine()
    time_based = engine.check_time_triggered_rituals("night")
    mood_based = engine.check_mood_triggered_rituals("anxious")

    if time_based:
        print("Time-based ritual:", time_based["default_text"])
    if mood_based:
        print("Mood-based ritual:", mood_based["default_text"])