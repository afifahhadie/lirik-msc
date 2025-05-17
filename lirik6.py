import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.12):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nThank God I found you, I was lost without you", 0.12),
        ("By every wish and every dream somehow became reality", 0.11),
        ("When you brought the sunlight, completed my whole life", 0.12),
        ("I'm overwhelmed with gratitude", 0.11),
        ("'Cause, baby, I’m so thankful I found you\n", 0.12),
    ]
    delays = [0.3, 5.8, 11.5, 17.3, 22.9]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()