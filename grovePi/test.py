#!/usr/bin/env python

import time
from grovepi import *

button = 4

pinMode(button, "INPUT")
time.sleep(1)

while True:
    try:
        # reading button state
        buttonState = digitalRead(button)
        print(buttonState)
        time.sleep(0.1)

    except KeyboardInterrupt:  # Turn Buzzer off before stopping
        break
    except IOError:  # Print "Error" if communication error encountered
        print("Error")
