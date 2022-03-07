### Exactly like the pyautogui autoclicker except using mouse

import mouse
from pynput.keyboard import Key, Listener, KeyCode
from time import sleep

# Global Settings
delay = 0.2  # Seconds
run_key = {Key.enter, KeyCode.from_char('l')}
current = set()
exit_key = Key.tab
paused = True
run = True

# Print out info for user
def info():
    print("Autoclicker created by Justin Garey")
    print(" - press 'enter' + 'l' to start up and pause")
    print(" - press 'tab' to end the program\n")

# What to do on key press
def on_press(key):
    global run, paused
    if key in run_key:
        current.add(key)
        if all(k in current for k in run_key):
            if paused == True:
                paused = False
                print("-- Auto Clicker Started --")
            else:
                paused = True
                print("-- Auto Clicker Paused  --")
    elif key == exit_key:
        run = False
        print("---- Exiting Program  ----")

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

# Main program body
def main():
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
    while run:
        if not paused:
            mouse.click('left')
            sleep(delay)
    listener.stop()

# If running this script
if __name__ == "__main__":
    info()
    main()