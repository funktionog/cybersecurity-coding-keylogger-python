### **Keylogger Python Program Documentation**

This Python program is a simple keylogger that records all keystrokes typed on a keyboard and saves them to a file named `keylog.txt`. It uses the **`pynput`** library to capture keyboard inputs and the **`logging`** module to store them in a log file.

---

### **How It Works:**
1. **Dependencies:**  
   - The program uses the `pynput.keyboard` module to monitor and log keyboard events.
   - The `logging` module is used to format and write the captured keystrokes to a log file.

2. **Log Configuration:**  
   - A log directory is defined (empty string in this case, meaning the log file will be saved in the same directory as the script).
   - The log file, `keylog.txt`, is created and configured to store entries with timestamps (`%(asctime)s`) and messages (`%(message)s`).

3. **Key Logging:**  
   - The function `keypress(Key)` is triggered whenever a key is pressed. This function converts the key event into a string and writes it to the log file.

4. **Listener Setup:**  
   - The `Listener` object monitors key presses using the `on_press` event. The program continues running and logging until manually stopped.

---

### **Important Notes:**
- **Ethical Usage:**  
  This program must only be used for educational purposes or on systems where you have explicit permission. Unauthorized use of keyloggers is illegal and unethical.
  
- **Improvement Potential:**  
  - Add error handling to prevent crashes.
  - Implement encryption for the log file to secure sensitive data.

This script demonstrates the basics of keylogging but should always be used responsibly and within legal boundaries.
