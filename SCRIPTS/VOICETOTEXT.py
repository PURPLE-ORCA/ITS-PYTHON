import speech_recognition as sr
import os
import datetime
from pathlib import Path
import time

obsidian_folder = Path(r"C:\Users\purple Orca\Documents\Obsidian Vault")
notes_folder = obsidian_folder / "vioce Notes"
os.makedirs(notes_folder, exist_ok=True)

recognizer = sr.Recognizer()

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
note_path = notes_folder / f"Voiced note{timestamp}.md"

with open(note_path, "w", encoding="utf-8") as file:
    file.write(f"# Voiced Note - {timestamp}\n\n")
print("🎙️ Live transcription started. Speak now...")
print("🔴 Say 'stop listening' to end transcription.")

def live_transcribe():
    """Continuously listen and write speech to a file in real-time."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                print("🎤 Listening...")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                
                if "stop listening" in text.lower():
                    print("🛑 Stopping transcription...")
                    break
                print(f"📝 {text}")  # Display live transcription
                with open(note_path, "a", encoding="utf-8") as file:
                    file.write(f" - {text}\n")
                os.utime(note_path, None)
                time.sleep(0.5)
            except sr.UnknownValueError:
                print("🤷 Couldn’t understand, try again...")
            except sr.RequestError:
                print("❌ Speech recognition service unavailable.")
                break

# Start live transcription
live_transcribe()

print(f"📄 Transcription saved in obsidian: {note_path}")
