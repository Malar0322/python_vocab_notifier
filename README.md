Python Vocabulary Notifier
A simple Tkinter GUI application that helps you grow your vocabulary by sending desktop notifications at regular intervals!
Built with Python, using Tkinter for the interface and Plyer for cross-platform notifications.

✨ Features
Displays vocabulary words from a local vocab.txt file as desktop notifications.
Clean, minimal GUI with a "NOTIFY" button to start
Background notification system using threading (so the app doesn't freeze).
Light, modern UI theme.
Easy to customize or extend with your own vocabulary list.

🚀 How It Works
Click the NOTIFY button.
The app reads words from vocab.txt.
Every 20 seconds, a new word (with meaning) pops up as a desktop notification.
Notifications automatically timeout after 15 seconds.

🛠️ Tech Stack
Python 3
Tkinter (GUI)
Plyer (for system notifications)
Threading (for smooth background tasks)

📥 Requirements
Python 3.x

Install dependencies:
pip install plyer
(Tkinter comes pre-installed with Python.)

📂 Project Structur
python_vocab_notifier/
│
├── vocab.txt          # List of vocabulary words
├── vocab_notifier.py  # Main application script
└── README.md    

