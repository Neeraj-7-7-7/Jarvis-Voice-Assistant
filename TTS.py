try:
    import pyttsx3
    import threading
except ModuleNotFoundError:
    import subprocess
    import threading
    subprocess.run("pip install pyttsx3")
    


def TTS(text):
    
    def speak(text):  
      E =  pyttsx3.init()
      E.setProperty('rate',150)
      v = E.getProperty('voices')
      E.setProperty('voice', v[1].id)
      E.say(text)
      E.runAndWait()
    
    TTS_thread = threading.Thread(target=speak, args=(text,), daemon=True)
    TTS_thread.start()
    
    

