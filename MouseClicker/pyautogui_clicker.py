### Based on python autoclicker by isaychris
### https://github.com/isaychris/python-autoclicker/blob/master/autoclicker.py

from pyautogui import click, position, PAUSE
from pynput.keyboard import KeyCode, Listener

# Global Settings
delay = 0.1  # Seconds
run_key = KeyCode(char='/')
exit_key = KeyCode(char='.')
paused = True
run = True

# Print out info for user
def info():
    print("Autoclicker created by Justin Garey")
    print(" - press '/' to start up and pause")
    print(" - press '.' to end the program")

# What to do on key press
def on_press(key):
    global run, paused
    if key == run_key:
        if paused == True:
            paused = False
            print("-- Auto Clicker Started --")
        else:
            paused = True
            print("-- Auto Clicker Paused  --")
    elif key == exit_key:
        run = False
        print("---- Exiting Program  ----")

# Main program body
def main():
    listener = Listener(on_press=on_press)
    listener.start()
    while run:
        if not paused:
            click(position())
            PAUSE = delay
    listener.stop()

# If running this script
if __name__ == "__main__":
    info()
    main()