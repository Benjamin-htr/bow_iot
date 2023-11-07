import time


class Timer:
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
        else:
            print("Timer has not been started yet.")
            return None

    def reset(self):
        """Method to reset the timer"""
        self.start_time = None
        self.elapsed_time = None
