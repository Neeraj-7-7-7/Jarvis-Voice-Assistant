import google.generativeai as genai

genai.configure(api_key="AIzaSyA_eaBpzBeFN7dbRqDT02kUsNFUJTuKTcI")

available_models = genai.list_models()
for model in available_models:
    print(model.name)








import threading
import speech_recognition as sr
import time
from Engine.TTS import TTS

sleep_mode = False  # Global flag to track sleep state
import subprocess
import sys
import pygame
import time
from Brain.voice import get_voice_features


# Initialize pygame for sound effects
pygame.mixer.init()

# Load sound effects
startup_sound = "sounds/startup.mp3"  # Change to your actual sound file
listening_sound = "C:/Users/email/Desktop/Jarvis/iron-man-repulsor.mp3"
import numpy as np

def verify_voice(audio):
    """Compares new voice input with the saved voiceprint"""
    try:
        new_voice = np.array(audio.frame_data, dtype=np.int16)
        similarity = np.corrcoef(user_voiceprint, new_voice)[0, 1]  # Compare audio signals
        
        return similarity > 0.85  # Adjust threshold (0.85 means 85% match)
    except Exception as e:
        print("Voice verification failed:", e)
        return False


def play_sound(sound_file, volume=0.05):
    """Play a sound effect at a specified volume before listening."""
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.set_volume(volume)  # Set volume (0.0 to 1.0)
    pygame.mixer.music.play()
    time.sleep(0.1)  # Wait for 


def listen_for_wake_command():
    """Continuously listens for 'Jarvis, wake up' while in sleep mode."""
    global sleep_mode
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Enjoy your time,sir.")
        TTS("Enjoy your time,sir.")

        while sleep_mode:  # Loop until woken up
            try:
                audio = r.listen(source, timeout=None)  # Always listening in sleep mode
                text = r.recognize_google(audio, language="en-IN").lower()
                if "jarvis wake up" in text:
                    print("At your service,sir")
                    TTS(f"At your service,sir")
                    sleep_mode = False
                    return  # Exit sleep mode and return to main STT loop
            except sr.UnknownValueError:
                continue  # Ignore unrecognized sounds
            except sr.RequestError:
                continue  # Ignore errors

def STT():
    global sleep_mode
    r = sr.Recognizer()
    r.dynamic_energy_adjustment_damping = 0.3
    r.dynamic_energy_ratio = 0.9
    r.pause_threshold = 0.5

    with sr.Microphone() as source:
        print("Listening...")
        play_sound(listening_sound)
        r.adjust_for_ambient_noise(source, duration=1)

        while True:
            if sleep_mode:
                listen_for_wake_command()  # Stay in wake-up listening mode
                continue  # Once woken up, restart STT loop

            try:
                audio = r.listen(source, timeout=120)  # Timeout after 120s of inactivity
                print("Processing...")
                text = r.recognize_google(audio, language="en-IN").lower()
                print(f"You said: {text}")

                if "jarvis go to sleep" in text:
                    sleep_mode = True
                    listen_for_wake_command()  # Switch to wake-up listening mode
                    continue  # Restart loop after waking up

                return text  # Return recognized command
                
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                continue
            except Exception as e:
                print(f"Error: {e}")
                continue
