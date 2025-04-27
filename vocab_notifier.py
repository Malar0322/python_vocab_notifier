import tkinter as tk
from tkinter import font
from plyer import notification
import time
import threading

def notify_vocab():
    title = "Learn Vocab"
    filename = "vocab.txt"
    try:
        with open(filename) as vc:
            lines = vc.readlines()
            for vocab in lines:
                notification.notify(
                    title=title,
                    message=vocab.strip(),
                    timeout=15,
                )
                time.sleep(20)
    except FileNotFoundError:
        print("Error: vocab.txt not found!")

def start_notification():
    # Run notification in a separate thread so that GUI does not freeze
    threading.Thread(target=notify_vocab, daemon=True).start()

# Create the main window
window = tk.Tk()
window.title("Vocabulary Notifier")
window.geometry("400x300")
window.config(bg="#F0F8FF")  # Light blue background

# Fonts
title_font = font.Font(size=20, weight='bold')
button_font = font.Font(size=14, weight='bold')

# Title Label
title_label = tk.Label(window, text="Grow your Vocabulary !", bg="#F0F8FF", fg="#333", font=title_font)
title_label.pack(pady=30)

# Notify Button
button = tk.Button(window, text="NOTIFY", command=start_notification,
                   fg="RED", bg="BLACK",
                   activebackground="blue", activeforeground="red",
                   font=button_font, width=15, height=2)

button.pack(pady=20)

# Run the app
window.mainloop()
