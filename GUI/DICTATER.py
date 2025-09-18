import customtkinter as ctk
import speech_recognition as sr
from pynput.keyboard import Controller as KeyboardController
import time
import threading
import os
from PIL import Image, ImageTk
import tkinter as tk

# --- Configuration ---
FOCUS_DELAY_SECONDS = 1.5
APP_TITLE = "Obsidian Voice Dictation"
PRIMARY_COLOR = "#37045F"  # Modern purple
SECONDARY_COLOR = "#000"  # Accent pink
BG_COLOR = "#000"  # Dark background
TEXT_COLOR = "#FFFFFF"  # White text
FONT_FAMILY = "Segoe UI" if os.name == "nt" else "Helvetica"

# --- Core Dictation Logic ---
keyboard = KeyboardController()
recognizer = sr.Recognizer()

class VoiceDictationApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("500x340")
        self.root.resizable(False, False)
        
        # Set appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.is_recording = False
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        self.frame = ctk.CTkFrame(self.root, fg_color=BG_COLOR)
        self.frame.pack(fill="both", expand=True)
        
        # Header with title and subtle gradient
        self.header_frame = ctk.CTkFrame(self.frame, fg_color=PRIMARY_COLOR, height=70, corner_radius=0)
        self.header_frame.pack(fill="x", padx=0, pady=(0, 15))
        
        self.title_label = ctk.CTkLabel(
            self.header_frame, 
            text=APP_TITLE,
            font=(FONT_FAMILY, 22, "bold"),
            text_color=TEXT_COLOR
        )
        self.title_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Status area with modern card design
        self.status_frame = ctk.CTkFrame(
            self.frame, 
            fg_color="#000",
            corner_radius=15,
            # border_width=1,
            # border_color="#3F3F5F"
        )
        self.status_frame.pack(fill="x", padx=25, pady=15, ipady=10)
        
        # Status label with icon
        self.status_label = ctk.CTkLabel(
            self.status_frame, 
            text="Ready to start dictation",
            font=(FONT_FAMILY, 16),
            text_color=TEXT_COLOR
        )
        self.status_label.pack(pady=15)
        
        # Animated indicator (pulses when recording)
        self.indicator_canvas = tk.Canvas(
            self.status_frame, 
            width=20, 
            height=20,
            bg="#2D2D42",
            highlightthickness=0
        )
        self.indicator_canvas.pack(pady=5)
        self.indicator = self.indicator_canvas.create_oval(2, 2, 18, 18, fill="#333333", outline="")
        
        # Dictation button - improved with hover effects
        self.button_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.button_frame.pack(pady=20)
        
        self.dictate_button = ctk.CTkButton(
            self.button_frame,
            text="Start Dictation",
            font=(FONT_FAMILY, 18),
            fg_color=PRIMARY_COLOR,
            hover_color=SECONDARY_COLOR,
            corner_radius=30,
            width=250,
            height=50,
            command=self.toggle_dictation
        )
        self.dictate_button.pack()
        
        # Footer with instructions
        self.footer_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.footer_frame.pack(fill="x", side="bottom", pady=15)
        
        self.footer_label = ctk.CTkLabel(
            self.footer_frame,
            text="Make sure Obsidian is focused before dictating",
            font=(FONT_FAMILY, 12),
            text_color="#AAAAAA"
        )
        self.footer_label.pack()
        
        # Initialize the pulsing animation (but not active)
        self.pulse_animation_active = False
        
    def toggle_dictation(self):
        if self.is_recording:
            # Nothing to do here as the recording function handles its own termination
            pass
        else:
            self.is_recording = True
            self.dictate_button.configure(state="disabled", text="Listening...")
            threading.Thread(
                target=self.record_and_type_into_obsidian,
                daemon=True
            ).start()
            
    def start_pulse_animation(self):
        self.pulse_animation_active = True
        self.pulse_size = 0
        self.pulse_growing = True
        self.animate_pulse()
            
    def stop_pulse_animation(self):
        self.pulse_animation_active = False
        self.indicator_canvas.itemconfig(self.indicator, fill="#333333")
            
    def animate_pulse(self):
        if not self.pulse_animation_active:
            return
            
        if self.pulse_growing:
            self.pulse_size += 0.1
            if self.pulse_size >= 1.0:
                self.pulse_growing = False
        else:
            self.pulse_size -= 0.1
            if self.pulse_size <= 0.0:
                self.pulse_growing = True
                
        # Calculate color based on pulse
        r = int(51 + 204 * self.pulse_size)  # 33 to 237
        g = int(51 + 50 * self.pulse_size)   # 33 to 83
        b = int(51 + 153 * self.pulse_size)  # 33 to 186
        color = f"#{r:02x}{g:02x}{b:02x}"
        
        self.indicator_canvas.itemconfig(self.indicator, fill=color)
        self.root.after(50, self.animate_pulse)
            
    def update_status(self, message, is_error=False):
        print(message)  # Keep console output for debugging
        
        if is_error:
            self.status_label.configure(text=message, text_color=SECONDARY_COLOR)
        else:
            self.status_label.configure(text=message, text_color=TEXT_COLOR)
            
        self.root.update_idletasks()  # Force GUI update
            
    def record_and_type_into_obsidian(self):
        self.update_status("Make sure Obsidian is active...")
        time.sleep(1)
        
        try:
            with sr.Microphone() as source:
                self.update_status("Adjusting for background noise...")
                time.sleep(0.5)  # Short pause instead of full adjustment
                
                self.update_status("Listening... Speak now")
                self.start_pulse_animation()
                
                try:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
                except sr.WaitTimeoutError:
                    self.update_status("No speech detected. Try again.", is_error=True)
                    self.stop_pulse_animation()
                    self.reset_button()
                    return
                    
            self.stop_pulse_animation()
            self.update_status("Transcribing...")
            
            text = recognizer.recognize_google(audio, language="ar-EG")
            
            if text:
                # Show a snippet of the transcribed text
                display_text = text[:30] + "..." if len(text) > 30 else text
                self.update_status(f"Transcribed: {display_text}")
                
                time.sleep(FOCUS_DELAY_SECONDS)
                keyboard.type(text)
                
                self.update_status("Text has been typed into Obsidian")
            else:
                self.update_status("No text was transcribed", is_error=True)
                
        except sr.UnknownValueError:
            self.update_status("Could not understand audio", is_error=True)
        except sr.RequestError as e:
            self.update_status(f"API Error: {e}", is_error=True)
        except Exception as e:
            self.update_status(f"Error: {e}", is_error=True)
        finally:
            self.reset_button()
            
    def reset_button(self):
        self.is_recording = False
        self.dictate_button.configure(state="normal", text="Start Dictation")
        self.stop_pulse_animation()

if __name__ == "__main__":
    root = ctk.CTk()
    app = VoiceDictationApp(root)
    root.mainloop()