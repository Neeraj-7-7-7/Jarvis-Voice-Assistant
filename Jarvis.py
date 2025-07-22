import sys
import os
import webbrowser
import re
import datetime
import requests

import pyautogui
import pyttsx3
from time import sleep
import random






# script_dir = os.path.dirname(os.path.abspath(__file__))

# engine_path = os.path.join(script_dir, "Engine")
# sys.path.append(engine_path)

# parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
# sys.path.append(parent_dir)





import webbrowser

strtime = datetime.datetime.now().strftime("%H:%M:%S")




import pywhatkit as kt
import threading
import speech_recognition as sr
import time


sleep_mode = False  # Global flag to track sleep state
import subprocess
import sys
import pygame
import time



# Initialize pygame for sound effects
pygame.mixer.init()

# Load sound effects
startup_sound = "sounds/startup.mp3"  # Change to your actual sound file
listening_sound = "C:/Users/email/Desktop/Jarvis1/iron-man-repulsor.mp3"
import numpy as np




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




import io
import threading
import pygame
import subprocess
from gtts import gTTS

# Ensure required libraries are installed
try:
    import pygame
    import gtts
except ModuleNotFoundError:
    subprocess.run("pip install gtts pygame", shell=True)

def TTS(text):
    """Converts text to speech using gTTS and plays it asynchronously with low delay"""

    def speak(text):
        try:
            # ✅ Generate speech & store in memory (No file saving)
            tts = gTTS(text, lang="en", tld="co.uk")
            audio_fp = io.BytesIO()  # Memory buffer
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)  # Move to start of buffer

            # ✅ Reinitialize pygame.mixer (Avoids 'mixer not initialized' error)
            pygame.mixer.init()
            pygame.mixer.music.load(audio_fp, "mp3")  # Load directly from memory

            # 🔊 Set volume (1.0 = max)
            pygame.mixer.music.set_volume(1.0)  # You can change this to e.g., 1.2 with sound amplification workaround (see note below)

            pygame.mixer.music.play()

            # Wait until playback is finished
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            pygame.mixer.music.unload()

        except Exception as e:
            print(f"❌ Error in TTS: {e}")

    # Run TTS in a separate thread to prevent blocking
    TTS_thread = threading.Thread(target=speak, args=(text,), daemon=True)
    TTS_thread.start()






    



try :
    import webbrowser
    import wikipedia
    import random
    import psutil
    import pyttsx3
    import os
    import psutil
    import GPUtil
    import pyttsx3
    import platform
    import requests
    
    import google.generativeai as genai

    import pyautogui
    import sounddevice as sd
    import subprocess
    import json
    
 


    
except ModuleNotFoundError:
    import subprocess 
    
import google.generativeai as genai    

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
    if battery is None:
        TTS("Sir, I couldn't retrieve battery information.")
        return

    percent = battery.percent
    is_plugged = battery.power_plugged
    remaining_time = battery.secsleft  # Time left in seconds

    status = "charging" if is_plugged else "not charging"
    time_left = "calculating..."

    # Convert remaining time to minutes
    if remaining_time != psutil.POWER_TIME_UNLIMITED and remaining_time > 0:
        hours = remaining_time // 3600
        minutes = (remaining_time % 3600) // 60
        time_left = f"{hours} hours and {minutes} minutes" if hours > 0 else f"{minutes} minutes"
        print(f"{time_left}")

    # Low battery warning
    if percent <= 20 and not is_plugged:
        TTS(f"Warning! Battery is critically low at {percent} percent. Please connect the charger immediately.")
    else:
        if is_plugged:
            TTS(f"Sir, the battery is at {percent} percent and is charging. It will be fully charged in approximately {time_left}.")
        else:
            TTS(f"Sir, the battery is at {percent} percent and the laptop is running on battery. Estimated remaining time is {time_left}.")

def next_song():
    """Simulate pressing Shift + N to play the next song in YouTube Music."""
    pyautogui.hotkey("shift", "n")
    print("Next song is playing...")

def previous_song():
    """Simulate pressing Shift + P to play the previous song."""
    pyautogui.hotkey("shift", "p")
    print("Playing previous song...")


def calc(text):
    text = str(STT()).lower()  # Assuming STT() is a speech recognition function
    text = text.replace("jarvis", "").strip()
    text = text.replace("calculate", "").strip()
    text = text.replace("multiply", "*")
    text = text.replace("plus", "+")
    text = text.replace("minus", "-")
    text = text.replace("divide", "/")

    final = str(text)

    try:
         result = eval(text)  # Calculate the result
         print(f"Jarvis: The answer is {result}")
         TTS(f"The answer is {result}")   
    
    except Exception as e:
        pass
    
    
def get_system_info():
    """Fetch and speak system information (CPU, GPU, RAM) using the provided tts function."""
    
    # Get CPU details
    cpu_info = platform.processor()
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq().max
    cpu_usage = psutil.cpu_percent(interval=1)

    # Get RAM details
    ram = psutil.virtual_memory()
    total_ram = round(ram.total / (1024**3), 2)  # Convert to GB
    available_ram = round(ram.available / (1024**3), 2)

    # Get GPU details (if available)
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]  # Take the first available GPU
        gpu_name = gpu.name
        gpu_memory = round(gpu.memoryTotal, 2)
    else:
        gpu_name = "No dedicated GPU detected"
        gpu_memory = "N/A"

    # Form the message
    message = f"""
    Sir, here is the system information.
    The CPU is {cpu_info} with {cpu_cores} cores and {cpu_threads} threads.
    The maximum CPU frequency is {cpu_freq:.2f} megahertz, and current usage is {cpu_usage} percent.
    The system has a total of {total_ram} gigabytes of RAM, with {available_ram} gigabytes available.
    The GPU in use is {gpu_name} with {gpu_memory} gigabytes of VRAM.
    """

    print(message)  # Show in terminal
    TTS(message)    
    
    


# Set your DeepSeek API key
# DEEPSEEK_API_KEY = "sk-6f95826baa104afdbfe6edbc140e7beb"
# deepseek_enabled = False

# def chat_with_deepseek(text):
#     text = str(STT()).lower()
#     """Ask DeepSeek AI a question and return the response."""
#     url = "https://api.deepseek.com/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "deepseek-chat",
#         "messages": [{"role": "user", "content": text}]
#     }

#     try:
#         response = requests.post(url, json=data, headers=headers)
#         response_data = response.json()
#         answer = response_data["choices"][0]["message"]["content"]
#         return answer
#     except Exception as e:
#         return f"Error: {str(e)}"
    
# def toggle_deepseek(command, TTS):
#     """Turn DeepSeek ON or OFF based on voice command."""
#     global deepseek_enabled

#     if "activate gpt" in command:
#         deepseek_enabled = True
#         print("DeepSeek Activated.")
#         TTS("DeepSeek is now activated.")
#     elif "deactivate gpt" in command:
#         deepseek_enabled = False
#         print("DeepSeek Deactivated.")
#         TTS("DeepSeek is now deactivated.") 
        
        
import requests

COHERE_API_KEY = "HmxunMmIw8AnQDqlpJEtKFCGKeBSAuWjYXmCqSJk"  # ← Replace this with your actual key

def chat_with_cohere(prompt):
    try:
        headers = {
            "Authorization": f"Bearer {COHERE_API_KEY}",
            "Content-Type": "application/json",
        }
        short_prompt = f"Answer in 2–3 short sentences only. Be concise:\n{prompt}"


        data = {
            "model": "command-r-plus",
            "prompt": short_prompt,
            "max_tokens": 150,
            "temperature": 0.7,
        }

        response = requests.post(
            "https://api.cohere.ai/v1/generate",
            headers=headers,
            json=data,
        )

        if response.status_code != 200:
            error_message = f"Error: {response.status_code} - {response.text}"
            print(error_message)
            TTS(error_message)
            return error_message

        output = response.json()["generations"][0]["text"].strip()

        print("Jarvis:", output)
        TTS(output)
        return output

    except Exception as e:
        error_message = f"Error: {str(e)}"
        print(error_message)
        TTS(error_message)
        return error_message


def shutdown():
    """Shutdown the computer immediately."""
    os.system("shutdown /s /t 0")  # Windows shutdown command

def restart():
    """Restart the computer immediately."""
    os.system("shutdown /r /t 0")  # Windows restart command

def log_off():
    """Log off the current user session."""
    os.system("shutdown /l")    
    
    
    
import pyautogui
import time
  # Import your text-to-speech function

def switch_audio_output():
    """Simulates pressing Win + Ctrl + V to switch audio output"""
    try:
        pyautogui.hotkey('win', 'ctrl', 'v')  # Press Windows + Ctrl + V
        time.sleep(0.1)
          
        print("Switched audio output device.")
        TTS("Switched to the next available audio output, sir.")
    
    except Exception as e:
        print(f"Error switching audio output: {e}")
        TTS("Failed to switch audio output, sir.")
        
def type_message(message):
    pyautogui.write(message, interval=0.05)  # Types like a human
    pyautogui.press('enter')        





    



           


    

   
       
               
     

      
        
        
        


    
# gemini_enabled = True  # Default: ON

# def toggle_gemini(state):
#     """Enable or disable Gemini AI."""
#     global gemini_enabled
#     gemini_enabled = state
#     status = "enabled" if state else "disabled"
#     TTS(f"Gemini AI has been {status}.")
#     print(f"Gemini AI is {status}.")    


while True :
        text = str(STT()).lower()  # ✅ Correct way

        text=text.lower()
        if "wikipedia" in text :
    
            text= text.replace("wikipedia","")
            text= text.replace("who is","")
            text= text.replace("what is","")
            TTS(get_answer(text))
            
        if "play" in text:
            text=text.replace("play  ","")   
            text=text.replace(" music ","")   
            kt.playonyt(text)
            TTS(f"Here is your music,sir")
            continue
            
        if "time" in text:
          strtime = datetime.datetime.now().strftime("%I:%M %p")  # 12-hour format with AM/PM
          print(f"The current time is {strtime}")
          TTS(f"The current time is {strtime}")    
             
            
        if "youtube" in text:
        
          text= text.replace("search","")
          text = text.replace(" youtube","")
          webbrowser.open(f"https://www.youtube.com/results?search_query={text}")
          TTS (f"you can see the result about {text} in your screen")
        
        
        if "search" in text:
        
          text= text.replace("search","")
          text = text.replace("on google","")
          webbrowser.open(f"https://www.google.com/search?q={text}")
          TTS (f"you can see the result about {text} in your screen")
        
        if "favourite song" in text:
         play_favourite_song()
            
            
            
        if "one tab" in text :
            pyautogui.hotkey("ctrl","w")
          
        if  "two tab" in text :
            pyautogui.hotkey("ctrl","w") 
            sleep(0.5)
            pyautogui.hotkey("ctrl","w") 
            TTS(f"Tabs has been closed sir")
        if "close"  in text :
            text= text.replace("windows","")
            
            pyautogui.hotkey("alt","f4") 
            TTS(f"Closing Window , sir")
            
        if "change tab"  in text :
            text= text.replace("tab","")
            
            pyautogui.hotkey("alt","tab") 
            TTS(f"switching tab , sir")
        if "stop" in text:
         text = text.replace("music", "")
         text = text.replace("the", "")
         pyautogui.press("space") 
        if "full screen" in text:
         text = text.replace("screen", "")
         pyautogui.press("f") 
        if "forward video" in text:
         text = text.replace("video", "")
         pyautogui.press("l")
         sleep(0.2) 
         pyautogui.press("l") 
         sleep(0.2) 
         pyautogui.press("l") 
         sleep(0.2) 
         pyautogui.press("l") 
         sleep(0.2) 
         pyautogui.press("l") 
         sleep(0.2) 
         pyautogui.press("l") 
        if "backward video" in text:
         text = text.replace("video", "")
         pyautogui.press("j") 
         sleep(0.2)
         pyautogui.press("j") 
         sleep(0.2)
         pyautogui.press("j") 
         sleep(0.2)
         pyautogui.press("j") 
         sleep(0.2)
         pyautogui.press("j") 
         sleep(0.2)
         pyautogui.press("j") 
        if "minimise" in text:
         text = text.replace("all windows", "")
         pyautogui.hotkey("win","d") 
         TTS(f"minimizing all windows ,sir")
        if "music on" in text:
         text = text.replace("music", "")
         pyautogui.press("space") 
        if "activate dark tab" in text:
         text = text.replace("activate", "")
         pyautogui.hotkey("ctrl","shift","n") 
         
         
        if "mute" in text:
            text=text.replace("jarvis","")
            pyautogui.press("volumemute")
            sleep(0.1)
            
        if "next" in text:
            text=text.replace("jarvis","")
            next_song()
        if "previous" in text:
            text=text.replace("jarvis","")
            previous_song()
        
            
        
        if "increase volume" in text:
            
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            sleep(0.1)
            pyautogui.press("volumeup")
            
       
        if "volume down" in text:
    
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown") 
            sleep(0.2)
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown")
            sleep(0.2)
            pyautogui.press("volumedown")
            
        # if "turn off ai" in text:
        #  toggle_gemini(False)

        # if "turn on ai" in text:
        #  toggle_gemini(True)
         
        # else:
        #     if gemini_enabled:
        #      chat_with_gemini(text)
        #     else:
        #      TTS("AI is turned off.")
        #      print("Gemini AI is OFF.")         
               
            
            
        if "open" in text:
            text = text.replace("open","")   
            text = text.replace("jarvis","")   
            pyautogui.press("super")
            pyautogui.typewrite(text)
            sleep(0.5)
            pyautogui.press("enter")
            
        if "gpt" in text.lower():  # Or use "ask", "question", etc.
           cleaned_prompt = text.replace("gpt", "").strip()
           chat_with_cohere(cleaned_prompt)

            
          
        if "hello" in  text:
            TTS(f"hello sir , how are you")
        if "hu r u" in  text:
            TTS(f"i am jarvis , sir , i can assist you with different task since best i can ")
            
          
            
        if "i am fine" in text.lower() :
            TTS(f"That's great ,sir")   
        # if "wake up" in text :
        #     text= text.replace("jarvis","")
        #     TTS(f"Online and ready to assist you ,sir") 
        if "battery" in text :
            text= text.replace("jarvis","")
            get_battery_status()
            
        if"system info" in text:
           text= text.replace("jarvis","")
           message = """"Sir, the system configuration is:
           CPU: Intel i7 (Base Clock Speed: 2.8 GHz)
           RAM: 16 GB
           GPU: NVIDIA GeForce GTX 1650 (VRAM: 4 GB)
           Storage is 1.25 Tera Byte """""
           print(message) 
           TTS(message)
        if "type" in text:
          text = text.replace("jarvis", "")
          text = text.replace("type", "")
          
          type_message(text.strip())

            
        if "how are you" in text:
            TTS(f"perfect ,sir")    
        if "Thanks" in  text:
            TTS(f"your are  welcome sir")
        if "send message" in text:
           kt.sendwhatmsg_instantly("+916200395292", "Hello")
           TTS(f"sending message, sir")
           
        # if "calculate" in text:
        #     text = text.replace("calculate","")
        #     text = text.replace("jarvis","")
        #     calc(text)
        
        if "restart" in text:
            text= text.replace("jarvis","")
            TTS("Restarting the system now.")
            sleep(3)
            restart()

        if "log off" in text or "sign out" in text:
            text= text.replace("jarvis","")
            TTS("Logging off, sir.")
            sleep(3)
            log_off()
        if "shutdown" in text:
             text= text.replace("jarvis","")
             TTS("Are you sure you want to shut down?")
             confirmation = STT()  # Listen for response
    
             if "ok" in confirmation:
              text= text.replace("jarvis","")  
              TTS("Shutting down now, sir.")
              sleep(3)
              shutdown()
             else:
                 TTS("Shutdown canceled.")
                 
                 


             
             
        if "calculate" in text.lower():  # Ensure text is lowercase for case-insensitive match
           print(f"Detected calculation command: {text}")  # Debugging print
           text = text.lower().replace("calculate", "").strip()
           text = text.replace("jarvis", "").strip()
           print(f"Processed text for calculation: {text}")  # Debugging print
           calc(text)  # Pass the cleaned-up text
    
        if "switch audio 1" in text:
         text= text.replace("jarvis","")
         pyautogui.hotkey('win', 'ctrl', 'v')  # Press Windows + Ctrl + V
         sleep(1)
         pyautogui.press('down')
         sleep(1)
         pyautogui.press('enter')
         sleep(1)
         pyautogui.hotkey("alt","tab") 
         TTS(f"Audio output changed")
        if "switch audio zero" in text:
         text= text.replace("jarvis","")
         pyautogui.hotkey('win', 'ctrl', 'v')  # Press Windows + Ctrl + V
         sleep(1)
         pyautogui.press('up')
         sleep(1)
         pyautogui.press('enter')
         sleep(1)
         pyautogui.hotkey("alt","tab")
         TTS(f"Audio output changed")
         
            
            
        # if "shutdown" in text:
        #     TTS(f"Enjoy your time, sir")
        #     exit() 
            
       
        
            
        
            
                  
          
        

        

                  
            
               
            

        
        
