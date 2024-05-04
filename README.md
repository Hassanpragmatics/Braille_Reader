# Braille Reader using Raspberry Pi

This Python script enables a Raspberry Pi to function as a Braille reader. It utilizes GPIO pins to control six electromagnetic pins, simulating Braille dots. Additionally, it incorporates audio feedback using the 'espeak' command for auditory assistance.

**Setup:**

**Hardware Setup:**
- Connect six electromagnetic pins to GPIO pins 40, 38, 36, 33, 35, and 37 of the Raspberry Pi.
- Ensure correct connections and polarity for the electromagnetic pins.

**Software Installation:**
- Install required Python libraries:
- Install 'espeak' for text-to-speech functionality:

**Running the Script:**
1. Place the Python script in a directory on the Raspberry Pi, preferably in the '/home/pi/' directory.
2. Open a terminal and navigate to the script directory.
3. Run the script using the following command:

**Usage:**

**Initial Setup:**
- Upon execution, the script initializes GPIO pins and sets up event detection for button presses.
- Ensure all connections are secure and functional before proceeding.

**Operating the Reader:**
- Press button GPIO 7 to start the system.
- The script scans '/home/pi/Documents' for readable files once started.
- Each readable file name is spoken aloud.
- Press button GPIO 8 to toggle audio feedback.
- Use buttons GPIO 10 and GPIO 11 to navigate forward and backward through text, respectively.
- Button GPIO 15 jumps to the end of the text.

**Reading Braille:**
- The script converts text to Braille format and activates corresponding electromagnetic pins for each character.
- Braille characters are displayed briefly before moving to the next character.

**Ending the Session:**
- The session ends automatically when all text has been read.
- To manually end the session, press Ctrl+C in the terminal.

**Notes:**
- Ensure correct circuit connections and GPIO pin assignments to avoid hardware malfunctions.
- Place all intended reading files in the '/home/pi/Documents' directory.
- This script is designed for educational purposes and may require modifications for specific applications or environments.
