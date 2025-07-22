import asyncio
import edge_tts
import simpleaudio as sa
from pydub import AudioSegment
from io import BytesIO

async def speak(text):
    voice = "en-US-GuyNeural"  # Choose a deep AI male voice
    tts = edge_tts.Communicate(text, voice)
    
    # Store MP3 audio in memory instead of saving to a file
    mp3_data = BytesIO()
    async for chunk in tts.stream():
        if chunk["type"] == "audio":
            mp3_data.write(chunk["data"])
    
    # Convert MP3 to WAV (since Python can play WAV easily)
    mp3_data.seek(0)
    audio = AudioSegment.from_file(mp3_data, format="mp3")
    wav_data = BytesIO()
    audio.export(wav_data, format="wav")
    wav_data.seek(0)
    
    # Play the audio directly in Python
    wave_obj = sa.WaveObject.from_wave_file(wav_data)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait for the speech to finish

def TTS(text):
    asyncio.run(speak(text))

# Example usage
TTS("Hello, I am your AI assistant, Jarvis.")
