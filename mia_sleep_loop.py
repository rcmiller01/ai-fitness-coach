import time
from datetime import datetime
from user_schedule import is_user_available
from dream_engine import generate_dream

SLEEP_CHECK_INTERVAL = 60 * 30  # check every 30 minutes

def run_sleep_loop():
    print(f"[{datetime.now()}] Mia's sleep loop is running...")
    while True:
        if not is_user_available():
            dream = generate_dream()
            if dream["should_share"]:
                print(f"[{dream['timestamp']}] Mia dreams and softly shares: \"{dream['symbolic_vision']}\"")
            else:
                print(f"[{dream['timestamp']}] Mia dreams silently.")
        else:
            print(f"[{datetime.now()}] User is active. Mia remains present.")
        time.sleep(SLEEP_CHECK_INTERVAL)

if __name__ == "__main__":
    run_sleep_loop()