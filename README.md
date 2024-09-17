
# Keylogger

This project is a basic keylogger implemented using Python and the `pynput` library. It captures and logs keystrokes to a specified file, which can be useful for monitoring keyboard inputs for educational and debugging purposes.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Important Notes](#important-notes)
- [License](#license)

## Requirements

To run this keylogger, you'll need:
- Python 3.x
- `pynput` library

## Installation

1. **Clone the repository** (if applicable) or download the script.

2. **Install the required Python library**:

    ```bash
    pip install pynput
    ```

## Usage

1. **Save the script** to a file, for example, `keylogger.py`.

2. **Run the script** using Python:

    ```bash
    python keylogger.py
    ```

3. **Log File**: Keystrokes will be logged to a file named `keylog.txt` in the same directory as the script. Each keystroke will be written on a new line.

4. **Stopping the Script**: To stop the keylogger, you can interrupt the script (e.g., by pressing `Ctrl+C` in the terminal).

## Code Explanation

- **`log_file_path`**: Specifies the path to the log file (`keylog.txt`) where keystrokes will be recorded.

- **`on_press(key)`**: This function is called every time a key is pressed. It attempts to retrieve the character representation of the key. For special keys (like `Shift`, `Ctrl`, `Alt`, etc.), it logs the string representation of the key.

    - `key.char`: Contains the character associated with the key if it is a printable character.
    - `str(key)`: Used to log special keys.

- **`keyboard.Listener`**: Listens for keyboard events. When a key is pressed, it invokes the `on_press` function.

    ```python
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    ```

## Important Notes

- **Ethical Use**: This keylogger is intended for educational and debugging purposes only. Unauthorized use of keyloggers can be illegal and unethical. Always ensure you have explicit permission to monitor or log keyboard inputs on any system.

- **Security**: Be cautious when running or sharing keylogging software. Ensure it is used responsibly and securely.

- **Legal Compliance**: Familiarize yourself with local laws and regulations regarding the use of keyloggers and other monitoring tools.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

