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
    
    import TTS


    
except ModuleNotFoundError:
    import subprocess 
    
import google.generativeai as genai    
from TTS import  TTS     
from STT import  STT     
    
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
        
        
GEMINI_API_KEY = "AIzaSyA_eaBpzBeFN7dbRqDT02kUsNFUJTuKTcI"  # Replace with your API key
genai.configure(api_key= "AIzaSyA_eaBpzBeFN7dbRqDT02kUsNFUJTuKTcI")


gemini_enabled = True

def chat_with_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        
        # 🔥 Force a direct, short answer (2-3 lines max)
        short_prompt = f"Answer in 2-3 sentences only: {prompt}"

        response = model.generate_content(short_prompt)
        answer = response.text.strip() if response else "I didn't understand that."

        # 🔹 Limit answer to max 2-3 sentences
        short_answer = ". ".join(answer.split(". ")[:2])  # Only take the first 2 sentences

        print("Jarvis:", short_answer)  # Print response
        TTS(short_answer)  # Speak response

        return short_answer

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





    



           


    

   
       
               
     

      
        
        
        
