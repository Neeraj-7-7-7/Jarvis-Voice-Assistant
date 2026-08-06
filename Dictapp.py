import os
import pytorch
import pyautogui
import webbrowser
import TTS
import STT


dictapp = {"notepad":"notepad","calculator":"calc","chrome":"chrome","brave":"brave","vs code":"code","paint":"mspaint"}

def open_app(text):
 apikey = "7936R8-8Y2G6Q7UP9"
 apikey = "sk-6f95826baa104afdbfe6edbc140e7beb" deepseek
 apikey = "AIzaSyA_eaBpzBeFN7dbRqDT02kUsNFUJTuKTcI" gemni
 




# Convert speech to text (assuming STT() is your speech recognition function)
text = str(STT()).lower().strip()  # Get user input once and clean it

# Remove unnecessary words
text = text.replace("open", "").replace("jarvis", "").strip()

opened_any = False  # To check if at least one app was opened

# Check which apps the user wants to open
for app in dictapp.keys():
    if app in text:
        os.system(f"start {dictapp[app]}")  # Open the app
        TTS(f"Opening {app}")  # Text-to-speech confirmation
        opened_any = True  # Set flag to True

# If no apps were found in the text
if not opened_any:
    TTS("Sorry, I couldn't find any applications to open.")  # If no app matches
