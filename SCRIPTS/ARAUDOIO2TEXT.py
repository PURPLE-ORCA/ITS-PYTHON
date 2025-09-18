import speech_recognition as sr
from pynput.keyboard import Controller
import time # To add a slight delay

# Initialize the keyboard controller
keyboard = Controller()

recognizer = sr.Recognizer()

# How long to wait after recognition before typing (gives you time to focus Obsidian)
# You can make this shorter if you're quick on the draw
FOCUS_DELAY_SECONDS = 1 

with sr.Microphone() as source:
    print("🎤 Obsidian is waiting... Make sure it's the active window!")
    print("   Start speaking in Arabic when ready...")
    try:
        recognizer.adjust_for_ambient_noise(source, duration=1) # Adjust for a second
        print("Listening...")
        audio = recognizer.listen(source) # This will block until a pause
    except Exception as e:
        print(f"Error with microphone or listening: {e}")
        exit()

print("🔍 Transcribing...")
try:
    text = recognizer.recognize_google(audio, language="ar-EG")
    print("📝 Transcription:")
    print(text)

    if text: # Only type if there's something to type
        print(f"\n✨ Typing into active window in {FOCUS_DELAY_SECONDS} sec...")
        time.sleep(FOCUS_DELAY_SECONDS) # Give yourself a moment to ensure Obsidian is focused

        # Type the text
        keyboard.type(text)
        
        # Optional: Add a space or a newline character after typing
        # keyboard.press(' ')
        # keyboard.release(' ')
        # or
        # keyboard.press(Key.enter)
        # keyboard.release(Key.enter)
        
        print("✅ Text typed!")

except sr.UnknownValueError:
    print("❌ Sorry, couldn't understand your voice.")
except sr.RequestError as e:
    print(f"⚠️ Could not request results from Google Speech Recognition service; {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")