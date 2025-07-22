import os
import google.generativeai as genai

GEMINI_API_KEY = "your-api-key-here"  # Replace with your API key
genai.configure(api_key= "AIzaSyA_eaBpzBeFN7dbRqDT02kUsNFUJTuKTcI")




def chat_with_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text.strip() if response else "I didn't understand that."
    except Exception as e:
        return f"Error: {str(e)}"
    
    
print(chat_with_gemini("who is elon musk in 2 lines"))    




try :
    import webbrowser
    import wikipedia
    import random
    import psutil
    import pyttsx3
    import wolframalpha
    import psutil
    import GPUtil
    import pyttsx3
    import platform
    import requests
    import google.generativeai as genai


    
except ModuleNotFoundError:
    import subprocess 
    subprocess.run('pip install wikipedia') 
    
from Engine.TTS import  TTS     
from Engine.STT import  STT     
    
def get_answer(text):
    try:
        return wikipedia.summary(text,sentences=2)
    except Exception :
        pass
    
def play_favourite_song():
    print("Playing your favourite song, sir")  # Assuming TTS() is a text-to-speech function
    TTS(f"Playing your favourite song, sir")  # Assuming TTS() is a text-to-speech function
    
    song_links = {
        1: "https://www.youtube.com/watch?v=_51KXfwcPMs&list=RD_51KXfwcPMs&start_radio=1",
        2: "https://www.youtube.com/watch?v=pHu4PLhuKgQ&list=RD_51KXfwcPMs&index=2",
        3: "https://www.youtube.com/watch?v=1gqBb4Y7LJA&list=RD_51KXfwcPMs&index=3",
        4: "https://www.youtube.com/watch?v=D49nMgP7Vzc&list=RD_51KXfwcPMs&index=4",
        5: "https://www.youtube.com/watch?v=nEnLt3pasxE&list=RD_51KXfwcPMs&index=5",
        6: "https://www.youtube.com/watch?v=JTOXKc5mUGU",
        7: "https://www.youtube.com/watch?v=CjWpWIw4bzc&list=PLXwdHknhd4HhNeSZrgxng2W56cMgP0dHh&index=11",
        8: "https://www.youtube.com/watch?v=FdyQoy7wwG0",
        9: "https://www.youtube.com/watch?v=W7LUCMUQFbU",
        10: "http://youtube.com/watch?v=9CmAUpXtVFc"
    }    
    
    random_song = random.choice(list(song_links.values()))  # Selects a random URL
    webbrowser.open(random_song)  
    
    
def get_battery_status():
     
     battery = psutil.sensors_battery()
     percent = battery.percent
     is_plugged = battery.power_plugged

     status = "charging" if is_plugged else "not charging"
     TTS(f"Sir, THe battery is currently running at {percent} percent, and the laptop is {status}.")
     
GEMINI_API_KEY = "your-api-key-here"  # Replace with your API key
genai.configure(api_key= "AIzaSyA_eaBpzBeFN7dbRqDT02kUsNFUJTuKTcI")


gemini_enabled = True

def chat_with_gemini(prompt):
    
    
    
    try:
        model = genai.GenerativeModel("gemini-pro")
        
        # Modify prompt to request a short answer
        short_prompt = prompt + " Give a short answer in 2-3 lines."
        
        response = model.generate_content(short_prompt)
        answer = response.text.strip() if response else "I didn't understand that."

        # Limit response to 2-3 lines
        short_answer = " ".join(answer.split(". ")[:2])  # Take first 2 sentences

        print("Jarvis:", short_answer)  # Print response
        TTS(short_answer)  # Speak response

        return short_answer

    except Exception as e:
        error_message = f"Error: {str(e)}"
        print(error_message)
        TTS(error_message)
        return error_message
    
    
    
import subprocess
import sys
import pygame
import time


# Initialize pygame for sound effects
pygame.mixer.init()

# Load sound effects
startup_sound = "sounds/startup.mp3"  # Change to your actual sound file
listening_sound = "C:/Users/email/Desktop/Jarvis/iron-man-repulsor.mp3"

def play_sound(sound_file, volume=0.05):
    """Play a sound effect at a specified volume before listening."""
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.set_volume(volume)  # Set volume (0.0 to 1.0)
    pygame.mixer.music.play()
    time.sleep(0.1)  # Wait for 



try:
    import speech_recognition as sr
except ModuleNotFoundError:
    subprocess.run([sys.executable, "-m", "pip", "install", "speechRecognition"])
    subprocess.run([sys.executable, "-m", "pip", "install", "pyaudio"])
    import speech_recognition as sr  # Import again after installing

def STT():
    r = sr.Recognizer()
    r.dynamic_energy_adjustment_damping = 0.3
    r.dynamic_energy_ratio = 0.9
    r.dynamic_energy_threshold = False
    r.pause_threshold = 0.5
    r.operation_timeout = None
    r.non_speaking_duration = 0.5

    with sr.Microphone() as source:
        print("Listening...", flush=True)
        play_sound(listening_sound)
        r.adjust_for_ambient_noise(source, duration=1)
        while True:
            try:
                ad = r.listen(source, timeout=None)
                print("Processing...", flush=True)
                text = r.recognize_google(ad, language="en-IN")
                print(f"You said: {text}")
                return text.lower()
            except sr.UnknownValueError:
                pass
                continue
            except sr.RequestError as e:
             pass
             continue
            
            
            
import os
import threading
import subprocess
import pygame
from gtts import gTTS

# Ensure required libraries are installed
try:
    import pygame
    import gtts
except ModuleNotFoundError:
    subprocess.run("pip install gtts pygame", shell=True)

def TTS(text):
    """Converts text to speech using gTTS and plays it asynchronously using pygame"""
    
    def speak(text):
        output_file = "jarvis_voice.mp3"  # Temporary file to store audio
        try:
            # Convert text to speech with a UK English voice
            tts = gTTS(text, lang="en", tld="co.uk")
            tts.save(output_file)  # Save as MP3
            
            # print(f"✅ Jarvis: {text}")

            # ✅ Reinitialize pygame.mixer every time before playing
            pygame.mixer.init()
            pygame.mixer.music.load(output_file)
            pygame.mixer.music.play()

            # Wait until playback is finished
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            # ✅ Do NOT quit the mixer after playback (fixes repeated error)
            pygame.mixer.music.unload()  # Unload instead of quitting

            os.remove(output_file)  # Delete the file after use

        except Exception as e:
            print(f"❌ Error in TTS: {e}")

    # Run TTS in a separate thread to prevent blocking the main program
    TTS_thread = threading.Thread(target=speak, args=(text,), daemon=True)
    TTS_thread.start()            
            
        
        


    
     