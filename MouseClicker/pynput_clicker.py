### Based on Geeks for Geeks pynput autoclicker
### https://www.geeksforgeeks.org/how-to-make-a-python-auto-clicker/
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Global Settings
delay = 0.1
button = Button.left
start_stop_key = KeyCode(char='/')
end_key = KeyCode(char='.')
  
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

# Print out info for user
def info():
    print("Autoclicker created by Justin Garey")
    print(" - press '/' to start up and pause")
    print(" - press '.' to end the program")

# What to do on key press
def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            print("-- Auto Clicker Paused  --")
        else:
            click_thread.start_clicking()
            print("-- Auto Clicker Started --")
    elif key == end_key:
        click_thread.exit()
        listener.stop()
        print("---- Exiting Program  ----")

# If running this script
if __name__ == '__main__':
    info()
    # Controller instance
    mouse = Controller()
    # Start a clicking thread
    click_thread = MouseClick(delay, button)
    click_thread.start()
    # Listener object
    with Listener(on_press=on_press) as listener:
        listener.join()

