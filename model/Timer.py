import time
import threading

class Timer:
    def __init__(self, duration=60):
        self.duration = duration
        self.remaining_time = duration
        self.is_running = False

    def start(self):
        if self.is_running:
            print("Le minuteur est déjà en cours.")
            return
        self.is_running = True
        self.timer_thread = threading.Thread(target=self._countdown)
        self.timer_thread.start()

    def _countdown(self):
        while self.remaining_time > 0:
            print(f"Temps restant : {self.remaining_time} secondes")
            time.sleep(1)
            self.remaining_time -= 1
        print("Minuteur terminé.")
        self.is_running = False

    def set_duration(self, duration):
        if not self.is_running:
            self.duration = duration
            self.remaining_time = duration
            print(f"Durée du minuteur réglée à {duration} secondes.")
        else:
            print("Impossible de changer la durée pendant que le minuteur est en cours.")

