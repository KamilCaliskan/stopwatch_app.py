import tkinter as tk
from tkinter import messagebox
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kronometre Uygulaması")
        self.root.geometry("300x200")
        
        self.start_time = None
        self.running = False
        self.elapsed_time = 0
        
        # Etiket
        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 30))
        self.time_label.pack(pady=20)
        
        # Düğmeler
        self.start_button = tk.Button(root, text="Başlat", command=self.start, width=10)
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Durdur", command=self.stop, width=10)
        self.stop_button.pack(pady=5)
        
        self.reset_button = tk.Button(root, text="Sıfırla", command=self.reset, width=10)
        self.reset_button.pack(pady=5)
        
    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            formatted_time = self.format_time(self.elapsed_time)
            self.time_label.config(text=formatted_time)
            self.root.after(100, self.update_time)
    
    def format_time(self, seconds):
        minutes, seconds = divmod(int(seconds), 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    
    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_time()
    
    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time
    
    def reset(self):
        if not self.running:
            self.elapsed_time = 0
            self.time_label.config(text="00:00:00")

def main():
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
