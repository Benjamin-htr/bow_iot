import time


class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = None

    def start(self):
        if self.start_time is not None:
            print("Timer is already running.")
        else:
            self.start_time = time.time()
            self.elapsed_time = None
            print("Timer started.")

    def stop(self):
        if self.start_time is None:
            print("Timer is not running.")
        else:
            self.elapsed_time = time.time() - self.start_time
            self.start_time = None

    def get_elapsed_time(self):
        if self.elapsed_time is not None:
            return self.elapsed_time
        elif self.start_time is not None:
            return time.time() - self.start_time
        else:
            print("Timer has not been started yet.")
            return None

    def reset(self):
        self.start_time = None
        self.elapsed_time = None
