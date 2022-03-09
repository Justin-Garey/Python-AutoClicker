import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key

# Global Settings
delay = 0.1
button = Button.left
start_end_key = KeyCode(char='g')
click_key = KeyCode(char='f')
press_key = KeyCode(char='r')
kill_key = KeyCode(char='h')
programRunning = True
  
# Mouse Click object
class MouseClick(threading.Thread):
    
    def __init__(self, delay, button):
        super(MouseClick, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
  
    def start_clicking(self):
        self.running = True
  
    def stop_clicking(self):
        self.running = False
  
    def exit(self):
        self.stop_clicking()
        self.program_running = False
  
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

# Mouse Press object
class MousePress(threading.Thread):
    
    def __init__(self, button):
        super(MousePress, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
  
    def start_clicking(self):
        self.running = True
  
    def stop_clicking(self):
        self.running = False
  
    def exit(self):
        self.stop_clicking()
        self.program_running = False
  
    def run(self):
        while self.program_running:
            while self.running:
                mouse.press(self.button)
            mouse.release(self.button)
            time.sleep(0.1)

# Print out info for user
def info():
    print("Autoclicker created by Justin Garey")
    print(" - press 'g' to start and stop the threads. You will lose some mouse functionality")
    print(" - press 'f' to start up and pause clicking")
    print(" - press 'r' to start up and pause long press")
    print(" - press 'h' to end the program")

# What to do on key press
def on_press(key):
    global programRunning
    if key == start_end_key:
        try:
            click_thread.start()
            press_thread.start()
            print("---- Threads Started  ----")
        except:
            click_thread.exit()
            press_thread.exit()
            listener.stop()
            print("--- Restarting Session ---")
    elif key == click_key:
        if click_thread.running:
            click_thread.stop_clicking()
            print("-- Auto Clicker Paused  --")
        else:
            click_thread.start_clicking()
            print("-- Auto Clicker Started --")
    elif key == press_key:
        if press_thread.running:
            press_thread.stop_clicking()
            print("-- Auto Presser Paused  --")
        else:
            press_thread.start_clicking()
            print("-- Auto Presser Started --")
    elif key == kill_key:
        click_thread.exit()
        press_thread.exit()
        listener.stop()
        print("---- Exiting Program  ----")
        programRunning = False


# If running this script
if __name__ == '__main__':
    info()
    while (programRunning):
        # Controller instance
        mouse = Controller()
        # Start a clicking thread
        click_thread = MouseClick(delay, button)
        # Start a press thread
        press_thread = MousePress(button)
        # Listener object
        with Listener(on_press=on_press) as listener:
            listener.join()

