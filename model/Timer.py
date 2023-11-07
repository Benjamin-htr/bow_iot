import time
import threading

class Timer:
<<<<<<< HEAD
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
=======
    """Class to represent a timer"""

    def __init__(self):
        self.start_time = None
        self.elapsed_time = None

    def start(self):
        """Method to start the timer"""
        if self.start_time is not None:
            print("Timer is already running.")
        else:
            self.start_time = time.time()
            self.elapsed_time = None
            print("Timer started.")

    def stop(self):
        """Method to stop the timer"""
        if self.start_time is None:
            print("Timer is not running.")
        else:
            self.elapsed_time = time.time() - self.start_time
            self.start_time = None

    def get_elapsed_time(self):
        """Method to get the elapsed time"""
        if self.elapsed_time is not None:
            return self.elapsed_time
        elif self.start_time is not None:
            return time.time() - self.start_time
>>>>>>> 1d6f4526aced7273007f0dcc81c94d07a4a10c7a
        else:
            print("Impossible de changer la durée pendant que le minuteur est en cours.")

<<<<<<< HEAD
=======
    def reset(self):
        """Method to reset the timer"""
        self.start_time = None
        self.elapsed_time = None
>>>>>>> 1d6f4526aced7273007f0dcc81c94d07a4a10c7a
