import tkinter as tk
import time

class Stopwatch:
    def __init__(self, master):
        self.master = master
        master.title("Stopwatch")

        self.time_elapsed = 0
        self.running = False
        self.start_time = 0

        self.label = tk.Label(master, text="00:00:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset, state=tk.DISABLED)
        self.reset_button.pack(pady=5)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.time_elapsed
            self.update()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.DISABLED)

    def stop(self):
        if self.running:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)

    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.label.config(text="00:00:00")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)

    def update(self):
        if self.running:
            self.time_elapsed = time.time() - self.start_time
            minutes = int(self.time_elapsed / 60)
            seconds = int(self.time_elapsed % 60)
            milliseconds = int((self.time_elapsed % 1) * 100)
            self.label.config(text=f"{minutes:02d}:{seconds:02d}:{milliseconds:02d}")
            self.master.after(10, self.update)
root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()
