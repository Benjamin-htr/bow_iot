import threading
import time


class Timer:
    """Class to create a timer"""

    def __init__(self, duration=60):
        self.duration = duration
        self.remaining_time = duration
        self.is_running = False
        self.timer_thread = None

    def start(self):
        """Method to start the timer"""
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
        """Method to set the duration of the timer

        Args:
            duration (int): Duration of the timer in seconds
        """
        if not self.is_running:
            self.duration = duration
            self.remaining_time = duration
            print(f"Durée du minuteur réglée à {duration} secondes.")

    def stop(self):
        """Method to stop the timer"""

        if not self.is_running:
            print("Le minuteur n'est pas en cours.")
            return
        self.is_running = False
        self.remaining_time = 0
        self.timer_thread.join()
        print("Minuteur arrêté.")
